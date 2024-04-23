const slides = document.querySelectorAll(".slide")  // class slide
var counter= 0;

// console.log(slides)      // const slides is printing while slide is class name

slides.forEach(
    (slide, index)=>  { 
            slide.style.left = `${index*100}%`   // it will shift the image like 0*100, 1*100,2*100
        }                                        // style="left: 0%; like that it will come in inpect
)
const GoNext=()=>{
    if(counter>1)
    {
        counter = 0;
        slideImage();
    }
    else{
        counter++;
        slideImage();
    }
}
const GoPre=()=>{
    if(counter==1 || counter==2)
    {
        counter--;  
        slideImage();     
    }
    else{
        counter = 2;
        slideImage();
    }
    
}

const slideImage = () =>{
    slides.forEach(
        (slide) =>{
            slide.style.transform = `translateX(-${counter*100}%)`
        }
    )
}

