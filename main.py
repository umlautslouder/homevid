function generatePassword(length, includeUppercase, includeLowercase, includeNumbers, includeSymbols) {
  let characters = '';
  let password = '';

  if (includeUppercase) {
    characters += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  }

  if (includeLowercase) {
    characters += 'abcdefghijklmnopqrstuvwxyz';
  }

  if (includeNumbers) {
    characters += '0123456789';
  }

  if (includeSymbols) {
    characters += '!@#$%^&*()_+-={}[]|:;"<>,.?/~`';
  }

  for (let i = 0; i < length; i++) {
    const randomIndex = Math.floor(Math.random() * characters.length);
    password += characters.charAt(randomIndex);
  }

  return password;
}

// Prompt the user for password preferences
const length = parseInt(prompt("Enter the desired password length:"));
const includeUppercase = confirm("Include uppercase letters?");
const includeLowercase = confirm("Include lowercase letters?");
const includeNumbers = confirm("Include numbers?");
const includeSymbols = confirm("Include symbols?");

// Generate the password
const password = generatePassword(length, includeUppercase, includeLowercase, includeNumbers, includeSymbols);

// Display the generated password
console.log("Generated Password:", password);
