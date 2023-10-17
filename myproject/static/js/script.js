// JavaScript to animate the text
    const textElement = document.getElementById("animatedText");
    const words = ["DevOps", "Web Development", "Machine Learning"];
    let wordIndex = 0;
    let letterIndex = 0;
    let isDeleting = false;
    const delayBetweenWords = 1000; // Delay between words in milliseconds
  
    function animateText() {
      const currentWord = words[wordIndex];
      const currentText = isDeleting
        ? currentWord.substring(0, letterIndex - 1)
        : currentWord.substring(0, letterIndex + 1);
  
      textElement.textContent = currentText;
  
      if (!isDeleting) {
        letterIndex += 1;
      } else {
        letterIndex -= 1;
      }
  
      if (letterIndex === currentWord.length + 1) {
        isDeleting = true;
      }
  
      if (isDeleting && letterIndex === 0) {
        isDeleting = false;
        setTimeout(nextWord, delayBetweenWords);
      } else {
        const speed = isDeleting ? 50 : 100;
        setTimeout(animateText, speed);
      }
    }
  
    function nextWord() {
      wordIndex = (wordIndex + 1) % words.length;
      setTimeout(animateText, 0);
    }
  
    animateText();