from .game import GameManager
from .session import SessionManager
from fastapi import WebSocket
import asyncio

async def game_handler_main(game: GameManager, websocket: WebSocket, session_id: str) -> None:
    
    while game.exists() and SessionManager(session_id).is_legit():
        
        data = await websocket.receive_json()

        sender_session = data.get('session')
        
        if sender_session != session_id:
            # Ignore messages from other sessions
            continue
        # Only leader commands
        if game.is_leader(session_id) and not game.started():
            
            if data.get('start_game'):
                await game.start()
                await asyncio.sleep(17)  # Wait for some time before starting the bot
                await game.bot_runner()

            if data.get('change_room_type'):
                game.change_room_type()
                await game.send_all_sockets(
                    {
                        'action':'room_type_change',
                        'room_type':game.room_type()
                    }
                )
                
        elif game.started():
            if game.get_turn() != game.get_color(session_id):
                # Ignore actions if it's not the player's turn
                continue

            action = data.get('action')
            if action == 'throw':
                throwing_card = data.get('thrown')
                wild_color = data.get('wild_color_send')

                # Validate if the player has the card to throw
                if throwing_card and (game.has_card(session_id, throwing_card) or game.has_card(session_id, f"{throwing_card.split('-')[0]}.png")):
                    await game.handle_card(game.get_color(session_id), throwing_card, wild_color)
                else:
                    continue
                
            elif action == 'draw':
                game.change_turn()
                await game.draw_card(game.get_color(session_id))

            await game.bot_runner()
    try:
        await websocket.close()
    except:
        pass

