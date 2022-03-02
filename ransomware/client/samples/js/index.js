/*

Snippet 1


*/

let customers = [
  { id: 0, name: "paul" },
  { id: 1, name: "jeff" },
  { id: 2, name: "mary" },
];

/*

Snippet 2


*/
let customer = customers.find((cust) => cust.name === "jeff");
console.log(customer);

/*

Snippet 3


*/
let myObject = { one: 1, two: 2, three: 3 };
Object.keys(myObject).forEach((key, value) => {
  //...do something
  console.log(key, value);
});

let data = [
  "files/dir1/file",
  "files/dir1/file2",
  "files/dir2/file",
  "files/dir2/file2",
];
let filteredData = data.filter((path) => path.includes("dir2"));
console.log(filteredData);
