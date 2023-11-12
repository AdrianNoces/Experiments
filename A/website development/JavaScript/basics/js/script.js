cost = 20.95
count = 2
cost2 = 7.99
tax = 0.1

amountOfTax = (cost + cost2 * count) * tax
amount = cost + cost2 * count

console.log("amount: ",amount,"\ntax: ",amountOfTax,"\ntotal: ", amount+amountOfTax);

// this is how to solve decimal without problems with computer's language , examples: 6.77 + 100.1 = 106.86999999999999//

wrong = 6.77 + 100.1
correct = Math.round(2095 + 799) / 100

console.log(correct);
console.log(Math.round(2.5));


h = Math.round((2095 + 799) * 0.1) / 100