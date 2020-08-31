//======================================================================================================================================================//
// Take your array and a friends array, write a function to merge both arrays into one (ordered lowest to highest) and remove duplicate numbers
//======================================================================================================================================================//
const myArray = [3, 4, 6, 7, 10, 11, 15, 16];
const friendsArray = [1, 5, 7, 8, 12, 14, 16, 19];

const mergeArrays = () => {
  console.log('My array: ' + myArray);
  console.log("My friend's array: " + friendsArray);
  let mergedArray = myArray.concat(friendsArray).sort(function(a, b) {
    return a - b;
  });
  console.log('Merged array: ' + mergedArray);
  let mergedArrayNoDups = mergedArray.filter(function(item, index) {
    return mergedArray.indexOf(item) >= index;
  });
  console.log('Merged array without duplicate values: ' + mergedArrayNoDups);
};

mergeArrays();

//======================================================================================================================================================//
// General Question: What are two-way data binding and one-way data flow, and how are they different?
//======================================================================================================================================================//
