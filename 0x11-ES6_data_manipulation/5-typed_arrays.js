export default function createInt8TypedArray(length, position, value) {
  try {
    return new DataView(new ArrayBuffer(length)).setInt8(position, value);
  } catch (error) {
    throw new Error('Position outside range');
  }
}
