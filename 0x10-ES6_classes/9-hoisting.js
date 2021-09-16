export class HolbertonClass {
  constructor(year, location) {
    this._year = year;
    this._location = location;
  }

  get year() {
    return this._year;
  }

  get location() {
    return this._location;
  }
}

export class StudentHolberton {
  constructor(firstName, lastName, holbertonClass) {
    this._firstName = firstName;
    this._lastName = lastName;
    this._holbertonClass = holbertonClass;
  }

  get fullName() {
    return `${this._firstName} ${this._lastName}`;
  }

  get holbertonClass() {
    return this._holbertonClass;
  }

  get fullStudentDescription() {
    return `${this.fullName} - ${this._holbertonClass.year} - ${this._holbertonClass.location}`;
  }
}

const class2019 = new HolbertonClass(2019, 'San Francisco');
const class2020 = new HolbertonClass(2020, 'San Francisco');
const allStudents = [
  ['Guillaume', 'Salva', class2020],
  ['John', 'Doe', class2020],
  ['Albert', 'Clinton', class2019],
  ['Donald', 'Bush', class2019],
  ['Jason', 'Sandler', class2019],
];
const result = [];

allStudents.forEach((student) => {
  result.push(new StudentHolberton(student[0], student[1], student[2]));
});

export default result;
