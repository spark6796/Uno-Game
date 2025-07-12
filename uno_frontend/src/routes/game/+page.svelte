
<script>
    import { onMount } from 'svelte';
    import { goto } from '$app/navigation';

    let game_id = $state('a259f')
    let session_id = null
    let im_leader = true
    let room_type = $state('private')
    let players = $state({
        'Spark':"pfp/2.jpg",
        'Frog':"pfp/4.jpg",
        'Squirtel':"pfp/5.jpg",
        'Panda':"pfp/1.jpg",
    });
    

    function sessionCheck(){
        session_id = sessionStorage.getItem('sessionid')
        if (session_id == null){
            alert('Invalid Session')
            goto('/')
            return
        }
    }
    

    function change_room_type(){}


    onMount(() => {
        // sessionCheck()
    })

</script>


<div id="main" class="flex justify-center items-center h-screen w-full bg-[#5472E4] overflow-hidden">   
    
    <div id="main_stuff" class="flex flex-col gap-12 items-center w-1/2 rounded-lg">

        <div class="inline-flex w-1/2">
            <button disabled={!im_leader} onclick={()=>{change_room_type()}} id="public" class="bg-blue-500 {room_type == 'public' ? 'border-4 border-blue-800 bg-blue-600' : ''} {im_leader ? 'hover:bg-blue-600':''} text-stone-200 text-4xl font-bold py-4 rounded-l w-full">
              Public
            </button>
            
            <div class="border-2 border-blue-600"></div>

            <button disabled={!im_leader} onclick={()=>{change_room_type()}} id="private" class="bg-blue-500 {room_type == 'private' ? 'border-4 border-blue-800 bg-blue-600' : ''} {im_leader ? 'hover:bg-blue-600':''} text-stone-200 text-4xl font-bold py-4 rounded-r w-full">
              Private
            </button>
        </div>

        <div class="text-white text-4xl"><span class="text-red-300 font-bold">Game ID:</span> {game_id}</div>
        <button class="w-1/2 border-4 rounded-full border-blue-800 bg-blue-500 animate-pulse p-5 text-white text-4xl {im_leader ? '': 'hidden'}">START</button>
        <div class="grid grid-cols-2 gap-y-4 gap-x-24 h-full w-full">

            {#each Object.entries(players) as [name, pfp]}
                <div class="flex border-blue-800 items-center border-8 p-4 rounded-full h-fit bg-blue-500 ">
                    <img src={pfp} alt="" class="border-4 border-blue-600 size-24 rounded-full">
                    <div class="text-4xl font-bold text-center text-white w-full">{name}</div>
                </div>
            {/each}
            
        </div>
    </div>
</div>