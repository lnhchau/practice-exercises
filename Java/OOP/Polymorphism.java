import java.util.ArrayList;
import java.util.List;
/*
 * Tính đa hình: là tính mở rộng của lớp con từ lớp cha, cho phép lớp con:
     - thay đổi nội dung phương thức
     - thay đổi giá trị thuộc tính
    của lớp cha. 

 */
class Animal {
  public void animalSound() {
    System.out.println("The animal makes a sound");
  }
}

class Pig extends Animal {
  public void animalSound() {
    System.out.println("The pig says: wee wee");
  }
}

class Dog extends Animal {
  public void animalSound() {
    System.out.println("The dog says: bow wow");
  }
}
public class Polymorphism {
    public static void main(String[] args) {
        Animal myAnimal = new Animal();  // Create a Animal object
        Animal myPig = new Pig();  // Create a Pig object
        Animal myDog = new Dog();  // Create a Dog object
        myAnimal.animalSound();
        myPig.animalSound();
        myDog.animalSound();
        /*
        Trong Java, tính đa hình còn được thể hiện mạnh ở biến tham chiếu, khi mà:
         - tạo nơi lưu địa chỉ object là lớp cha (Ví dụ: Animal myPig)
         - địa chỉ dẫn tới object là lớp con (new Pig())

        Qua đó cho phép tạo ra một ArrayList gồm nhiều object con khác nhau, và các class con đều được kế thừa từ lớp cha.
        */ 
        List<Animal> myFarm = new ArrayList<>();
        myFarm.add(myPig);
        myFarm.add(myDog);
      }
}
