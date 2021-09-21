export default function createInt8TypedArray(length, position, value) {
  try {
    const buffer = new ArrayBuffer(length);
    const dataview = new DataView(buffer);
    dataview.setInt8(position, value);
    return dataview;
  } catch (error) {
    throw new Error('Position outside range');
  }
}
