function playTheGame() {
    const willPlay = confirm("Do you want to play the game?");
    if (!willPlay){
        alert("No Problem. Goodbye")
    } else {
        let number;
        while (true){
            number = Number(prompt("Enter a number between 1 and 10: "));
          if (isNaN(number)) {
            alert("Sorry. Not a number.Goodbye")
            // return ""
            continue;
          }
          if (number < 1 || number > 10) {
            alert("Sorry it's not a good number. Goodbye");
            // return ""
            continue;
          }

          break;
        }

        let computerNumber = Math.floor(Math.random() * 10) + 1;

        compareNumbers(number,computerNumber);
    }

}

function compareNumbers(userNumber, computerNumber) {
    let chances = 1
    while (chances < 3) {
        if (userNumber == computerNumber) {
            alert("Winner")
            break;
        } else {
            chances = chances + 1
            if (userNumber > computerNumber) {
                userNumber = Number(prompt("Your number is bigger then the computer’s, guess again"));
            } else {
                userNumber = Number(prompt("Your number is smaller then the computer’s, guess again"))
            }
        }
    }
    alert("out of chances");
    return ""
}