/*Encapsulation là tính chất đóng gói, nghĩa là một class có thể có chứa:
 * - thuộc tính (Attribute), ví dụ như: String data, String name, int age
 * - phương thức (method), ví dụ như: void setName(String name), int getAge()
 * Uses cases: Để kiểm soát phạm vi sử dụng của các thành phần trong class, 
 Java define ra các access modifier cho từng thành phần:
    - public: thuộc tính và phương thức được truy cập ở khắp nơi trong package.
    - protected: thuộc tính và phương thức được truy cập ở trong class và trong các class con.
    - private: thuộc tính và phương thức được truy cập ở trong class
 */
public class Encapsulation {
    private String data; // định dạng data là private, thì data chỉ được gọi trong class Encapsulation thôi.
    public Encapsulation(){}

    public String getter(){
        /*
         * Hàm getter dùng để trả về cho người dùng giá trị data 
         (khi mà data là private và không thể truy cập trực tiếp bên ngoài class)
         Return: String data
         Hàm getter giúp lập trình viên kiểm soát khi nào người dùng lấy biến data và kiểm soát giá trị trả về cho người dùng.
         */
        return "data is checked by getter: "+data; // ví dụ cho việc gọi `data` trong class Encapsulation
    }

    public void setter(String input_from_user){
        /*
         * Hàm setter dùng để set giá trị thuộc tính data 
         (khi mà data là private và không thể gán trực tiếp bên ngoài class)
         No return 
         Hàm setter dùng để tránh việc người dùng set giá trị trực tiếp từ bên ngoài class cho biến data. 
         Qua đó kiểm soát được giá trị của người dùng muốn set là gì và đưa ra rule.
         */
        if (input_from_user.equals("dmcs")){
            data = "invalid from user";
        }
        else{
            data = input_from_user;
        }
    }

}
