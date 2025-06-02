const search = (arr, num) => {
  let left = 0;
  let right = arr.length - 1;
  let mid = Math.floor((left + right) / 2);
  while (left <= right) {
    if (arr[mid] === num) {
      return;
    } else if (arr[mid] < num) {
      left = mid + 1;
      mid = Math.floor((left + right) / 2);
    } else if (arr[mid] > num) {
      right = mid;
      mid = Math.floor((left + right) / 2);
    }
  }
};
const t1 = [1, 3, 5, 7, 9];
const t = search(t1, 4);
