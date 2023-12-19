import java.util.ArrayList;

/**
 * Abstract class representing a generic shape.
 */
abstract class Shape {

    /**
     * Abstract method to get the area of the shape.
     *
     * @return The area of the shape.
     */
    protected abstract double getArea();

    /**
     * Abstract method to get the perimeter of the shape.
     *
     * @return The perimeter of the shape.
     */
    protected abstract double getPerimeter();

    /**
     * Prints information about the shape, including its area and perimeter.
     */
    protected void getInfo() {
        System.out.println("The Area: " + getArea());
        System.out.println("The Perimeter: " + getPerimeter());

    }
}

/**
 * Class representing a rectangle, a specific type of shape.
 */
class Rectangle extends Shape {

    private double width;
    private double height;

    /**
     * Constructor for the Rectangle class.
     *
     * @param width  The width of the rectangle.
     * @param height The height of the rectangle.
     */
    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }

    /**
     * Calculates and returns the area of the rectangle.
     *
     * @return The area of the rectangle.
     */
    public double getArea() {
        double area = this.width * this.height;
        return area;
    }

    /**
     * Calculates and returns the perimeter of the rectangle.
     *
     * @return The perimeter of the rectangle.
     */
    public double getPerimeter() {
        double perimeter = (this.width + this.height)*2;
        return perimeter;
    }
}

/**
 * Class representing a square, a specific type of shape.
 */
class Square extends Shape {

    private double side;

    /**
     * Constructor for the Square class.
     *
     * @param side The side length of the square.
     */
    public Square(double side) {
        this.side = side;
    }

    /**
     * Calculates and returns the area of the square.
     *
     * @return The area of the square.
     */
    public double getArea() {
        double area = this.side*this.side;
        return area;
    }

    /**
     * Calculates and returns the perimeter of the square.
     *
     * @return The perimeter of the square.
     */
    public double getPerimeter() {
        double perimeter = this.side*4;
        return perimeter;
    }
}

/**
 * Main class demonstrating the Shape system.
 */
public class Shape_system {

    /**
     * Main method to create shapes and print their information.
     * 
     * @param args Command-line arguments (not used in this example).
     */
    public static void main(String args[]) {
        ArrayList<Shape> shapes = new ArrayList<Shape>();
        shapes.add(new Rectangle(5.0, 3.0));
        shapes.add(new Square(4.0));
        shapes.add(new Rectangle(1.0, 2.0));

        for (int i = 0; i < shapes.size(); i++) {
            shapes.get(i).getInfo();
        }
    }
}