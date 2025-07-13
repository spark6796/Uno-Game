
<script>
    import { onMount } from 'svelte';
    import { gsap } from "gsap";
    import { goto } from '$app/navigation';
    
    let deck = [
        'green/5.png',
        'red/0.png',
        'special/wild.png',
        'yellow/+2.png',
        'green/reverse.png',
        'blue/skip.png',
        'yellow/4.png',
        'green/2.png',
        'blue/4.png',
        'red/6.png',
        'special/+4.png',
        'red/4.png'
    ]
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
    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
    function shuffleHTMLCollection(htmlCollection) {
            const array = Array.from(htmlCollection);
            for (let i = array.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [array[i], array[j]] = [array[j], array[i]];
            }
            return array;
    }
    
    function splitArrayInTwo(arr) {
        const middleIndex = Math.ceil(arr.length / 2);
        const firstHalf = arr.slice(0, middleIndex);
        const secondHalf = arr.slice(middleIndex);
        return [firstHalf, secondHalf];
    }
    function shuffle_deck(){
            let my = document.getElementById('distributer')
            let my_parent = document.getElementById('deckk')
            let my_childs = my_parent?.children
            let shuffled_array = shuffleHTMLCollection(my_childs)
            let my_arrays = splitArrayInTwo(shuffled_array)

            // SHUFFLE RIGHT
            for (let i in my_arrays[0]){
                sleep(1000*i).then(
                    ()=> {
                    gsap.to(
                    my_arrays[0][i],
                    { x:'28vh' ,zIndex:i, duration: 1 ,}
                    )

                sleep(1000).then(
                    ()=>{
                    gsap.to(
                    my_arrays[0][i],
                    { x:0 ,zIndex:i, duration: 1 ,}
                    )})

                })
                
                }
            // SHUFFLE LEFT
            for (let i in my_arrays[1]){

                sleep(1000*i).then(
                    ()=> {
                    gsap.to(
                    my_arrays[1][i],
                    { x:'-28vh' ,zIndex:i, duration: 1}
                    )

                sleep(1000).then(()=>{
                    gsap.to(
                    my_arrays[1][i],
                    { x:0 ,zIndex:i, duration: 1}
                    )})

                })
                
                }
            sleep(my_arrays[0].length+my_arrays[1].length*1000+1000).then(()=>{
                gsap.to(
                my_parent, {rotateY:90,onComplete: ()=>{
                    my_parent.className+=' hidden'
                    my.classList.replace('hidden','flex')
                    gsap.from(
                        my,{rotateY:-90,onComplete: ()=>{
                        let my_shuffle_text = document.getElementById('shuffle_text')
                        gsap.to(
                            my_shuffle_text,{opacity:0,duration:1,onComplete: ()=>{my_shuffle_text.hidden = true}}
                        )
                    }}
                    )
                }}
                )
            })
            }
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
        sleep(1000).then(()=>{
            sessionCheck()
        })
    })

</script>


<div hidden id="main" class="flex justify-center items-center h-screen w-full bg-[#5472E4] overflow-hidden">   
    
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


<div id="game" class="max-h-screen h-screen max-w-full overflow-hidden bg-[#5472E4]">


<div class="absolute h-1/2 w-full">
        <div id="deckk" class="flex h-full w-full h justify-center items-end">
            {#each deck as card}
                <img alt={card} src="cards/{card}" class="absolute rounded-[2.9rem] h-2/3 w-[14%]">
            {/each}
            
        </div>
       
</div>


</div>