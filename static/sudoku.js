const seclink = document.getElementsByClassName("l2")[0]
seclink.addEventListener("mouseover", () => {
    document.getElementsByClassName("l1")[0].style.marginTop = "33vh"
    seclink.addEventListener("mouseout",() => {
        document.getElementsByClassName("l1")[0].style.marginTop = "35vh"
    })
})


const smallsquare = document.getElementsByClassName("squareinp")
for (let ind = 0; ind < smallsquare.length; ind++) {
    const element = smallsquare[ind];
    element.addEventListener("keyup", function(event){
        if (!"1234567890".includes(element.value)){
            element.value = "0"
        } else if((event.key == element.value || event.keyCode == 39) && ind != smallsquare.length-1){
            smallsquare[ind+1].focus()
        } else if(event.keyCode == 37 && ind != 0){
            smallsquare[ind-1].focus()
        }

        })    
}














