class Car_2 {
    private String brand;
    private String number_plate;

    // Constructor for Car_2
    public Car_2(String brand, String number_plate) {
        /*
        Từ khóa this dùng để phân biệt giữa biến của class và tham số
        Nếu tham số có tên khác với tên biến của class thì có thể không cần dùng this.
        */ 
        this.brand = brand;
        this.number_plate = number_plate;
    }
    // Một class có thể có nhiều constructor, chỉ cần khác parameter truyền vào. 
    public Car_2(){
        this.brand = "BMW";
        this.number_plate = "000";
    }


    // Getter methods for brand and number_plate

    public String getBrand() {
        return brand;
    }

    public String getNumberPlate() {
        return number_plate;
    }
}

public class Constructor {
    public static void main(String[] args) {
        Car_2 car = new Car_2("Toyota", "ABC123");
        /*
         * 1. biến tên car: là biến tham chiếu vì chỉ lưu địa chỉ của object
         * 2. new Car_2(): sẽ tạo object Car_2 dựa theo hàm khởi tạo
         * 3. chỉ gán địa chỉ của object Car_2 vào biến car (không phải gán object vào biến car)
         */
    }
}