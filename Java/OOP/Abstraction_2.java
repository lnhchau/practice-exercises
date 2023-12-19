/*
 * Interface là một dạng abstract class đặc biệt khi:
 * - chỉ chứa phương thức (method)
 * - tất cả method đều là abstract. 
 * Cho nên khi kế thừa từ Interface thì người ta dùng từ khóa `implement` nghĩa là ghi nội dung thực thi vào từng phương thức trong interface.
 * Class có thể được kế thừa nhiều hơn 1 các interface khác nhau.
 */
interface FirstInterface {
  public void myMethod(); // interface method
}

interface SecondInterface {
  public void myOtherMethod(); // interface method
}

// DemoClass là lớp kế thừa từ 2 interface, cho nên phải có nghĩa vụ ghi nội dung thực thi ở tất cả các hàm ở 2 interface.
class DemoClass implements FirstInterface, SecondInterface {
  public void myMethod() {
    System.out.println("Some text..");
  }
  public void myOtherMethod() {
    System.out.println("Some other text...");
  }
}

public class Abstraction_2 {
    public static void main(String[] args) {
        DemoClass myObj = new DemoClass();
        myObj.myMethod();
        myObj.myOtherMethod();
      }
}