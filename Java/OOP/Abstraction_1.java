/*
 * Abstraction là tính trừu tượng của lớp, cho phép một lớp có tính trừu tượng, mô tả khái quát nhưng không gồm các chi tiết.
 * Abstraction giúp người frontend user hiểu:
    - class này là gì
    - method có input/output gì
    - ý nghĩa của từng method là gì
   Còn về cách vận hành và chạy thì sẽ được class con kế thừa và implement. 

  * Note: Một điều bắt buộc là khi lớp cha đã define phương thức abstract thì lớp con phải viết nội dung vào phương thức đó. 
 */
abstract class Animal {
  // Abstract method (does not have a body)
  public abstract void animalSound();
  // Regular method
  public void sleep() {
    System.out.println("Zzz");
  }
}

// Subclass (inherit from Animal)
/*
Và lớp Pig bắt buộc phải ghi nội dung vào phương thức animalSound() vì lớp cha đã set phương thức này là abstract.
Lớp Pig không cần phải ghi nội dung của phương thức sleep() vì không phải là abstract method.
*/ 
class Pig extends Animal {
  public void animalSound() {
    // The body of animalSound() is provided here
    System.out.println("The pig says: wee wee");
  }
}
public class Abstraction_1 {
    public static void main(String[] args) {
    Pig myPig = new Pig(); // Create a Pig object
    myPig.animalSound();
    myPig.sleep();
  }
}
