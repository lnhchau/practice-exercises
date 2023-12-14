/*
 * Inheritance là tính chất của OOP, cho phép một lớp kế thừa (sở hữu) những:
 thuộc tính và phương thức của lớp được kế thừa (lớp cha). 
 Qua đó, cho phép:
    - lớp kế thừa (lớp con) mở rộng từ lớp cha (thuộc tính chất Polymorphism).
    - lớp được kế thừa (lớp cha) trở nên trừu tượng, đơn giản hóa và thông tin chi tiết sẽ được implement cho lớp con (thuộc tính chất Abstraction).
Inheritance chỉ cho phép kế thừa từ class cha những thuộc tính và phương thức là:
    - protected
    - public
 */
class Vehicle {
  protected String brand = "Ford";        // Vehicle attribute
  public void honk() {                    // Vehicle method
    System.out.println("Tuut, tuut!");
  }
}

// Lớp Car kế thừa từ Vehicle, và sở hữu hết các thuộc tính, phương thức public hoặc protected của lớp Vehicle.
class Car extends Vehicle {
  public String modelName = "Mustang";    // Car attribute
}

public class Inheritance {
    public static void main(String[] args) {

    // Create a myCar object
    Car myCar = new Car();

    // Call the honk() method (from the Vehicle class) on the myCar object
    myCar.honk();

    // Display the value of the brand attribute (from the Vehicle class) and the value of the modelName from the Car class
    System.out.println(myCar.brand + " " + myCar.modelName);
  }
}
