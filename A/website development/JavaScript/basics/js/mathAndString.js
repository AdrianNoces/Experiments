soup = 10;
burgers = 8;
icecream = 5;

order = (soup + icecream) + burgers * 3
console.log("total cost of the order is",order,",3 people will pay",order*3/3,"each, with a total of",order*3);



toaster = 1850;
shirts = 750;

tax = Math.round((toaster + shirts * 2) * 0.1) / 100;

tax2 = Math.round((toaster + shirts * 2) * 0.2) / 100;

cost = Math.round(toaster + shirts * 2) / 100;

console.log("the total cost is",cost,", with a 10% tax it is",cost+tax,", the total of tax is",tax);

console.log("the total cost is",cost,", with a 20% tax it is",cost+tax2,",the total of tax is",tax2);


/* to calculate decimal without error make them whole number calculate then devide it with 100 to go back to decimal */
items = 4793;
shipping = 499;
beforeTax = Math.round(items + shipping) / 100;
tax = Math.round((items + shipping) * 0.1) / 100;
totalOrder = beforeTax + tax;

h = "\n";

console.log("items:",items/100,"shipping:", shipping/100,"before tax:", beforeTax,",10% tax:", tax, "Order total:",totalOrder);



/* this only round up a decimal number*/
console.log(Math.ceil(2.2));
/* this only round down a decimal number*/
console.log(Math.floor(2.8));

/* calculate numbers and add strings*/
str = '$' + ((2095 + 799) / 100);
items = 'items (' + (1+1) + '): $' + ((2095 + 799) / 100);
/* double quotes can make single quotes a string*/
console.log(str);
console.log(items);

/* double quotes*/
console.log("I'am adrian");

/* single quotes use for default string*/
console.log('hello');

/* use interpolation back ticks or template string*/
console.log(`items (${ 1 + 1}): $${((2095 + 799) / 100)}`);

coffee = 599;
bagel = 295;

h = `Total cost: $${(coffee+bagel)/100}\nThank you,come again!`;
alert(h);

basketball = 2095;
shirt = 799;

total = `items (${2+2}): $${((basketball*2)+(shirt*2))/100} Shipping and handling $${((499*2)/100)} Total before tax: ${(((basketball*2)+(shirt*2))/100)+((499*2)/100)} Estimated tax(10%): ${6.79} Order total: ${((((basketball*2)+(shirt*2))/100)+((499*2)/100))+6.79}`;


