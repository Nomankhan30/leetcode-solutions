function merge(nums1: number[], m: number, nums2: number[], n: number): void {
  let i: number = m - 1;
  let j: number = n - 1;
  let k: number = m + n - 1;

  while (i >= 0 && j >= 0) {
    if (nums1[i] > nums2[j]) {
      nums1[k] = nums1[i];
      i--;
    } else {
      nums1[k] = nums2[j];
      j--;
    }
    k--;
  }

  //Copy remaining elements of nums2 (if any)
  while (j >= 0) {
    nums1[k] = nums2[j];
    j--;
    k--;
  }
}
