export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  static get [Symbol.newobj]() {
    return this;
  }

		cloneCar() {
			return new Car(this._brand, this._motor, this._color);
	}
}
