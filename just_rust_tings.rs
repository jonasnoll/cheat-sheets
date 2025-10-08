// Just Rust Things to reuse

// Run ------------------------------------------------------------------------
// Use cargo to create a project 
cargo new hello_cargo
// Use build to cteate an executable run it in the target/debug folder
cargo build 
./target/debug/hello_cargo
// But just use cargo run to compile and run it at the same time 
cargo run
// If you want to release it you build it via: 
cargo build --release // (built with optimizations)



// Variables ------------------------------------------------------------------------
let x: i32 = 5;
let s: &str;

// Numbers
// Signed (Positive & Negative) & unsigned (always positive)
let i: i8; // signed 8-bit
let j: u32; // unsigned 32-bit 
// Defaults (Comiler referrs it to...): 
let x: i32; // integers <--
let y: f64: // floats <--
// Type annotation: _u8
let v: u16 = 38_u8 as u16;
// Stellen runden 
assert!(9.6 as f32 / 3.2 as f32 == 3.0 as f32);

// Char
// Make it work
let c1: char: 'a';
let c1: char = "中"; // is wrong! because "" are for strings
use std::mem::size_of_val;
fn main() {
    let c1 = 'a';
    assert_eq!(size_of_val(&c1),4); 
    let c2 = '中';
    assert_eq!(size_of_val(&c2),4); 
    println!("Success!");
} 

// Unit
// Empty Touble of size 0 bytes, used to return "nothing"
let unit: () = ();


// Expresseions ---------------------------------------------------------------------
// Zuweisung durch weglassen von ;
// Make it work with two ways
fn main() {
	let v = {
		let mut x = 1;
		x + 2
	};
	assert_eq!(v, 3);
	println!("Success!");

	let u = sum(v + 1);
}
fn sum(x: i32, y: i32) -> i32 {
	x + y
}


// Functions ------------------------------------------------------------------------
fn define_x() {
    let x: &str  = "hello";
    println!("{}, world", x); 
};

// Functions always have to specify their types
// especially Output types otherwise () is used
fn sum(x, y: i32) -> i32 {
    x + y
}

// Diverging Functions
// Never return to the caller
// Example Panic function - Program exits
fn never_return() -> ! {
    panic!()
}

// Shadowing ------------------------------------------------------------------------
// We can declare and init variables with the same name in a different scope
fn main() {
    let x: i32 = 5;
    {
    	// init new variable x because new scope
        let x = 12;
        assert_eq!(x, 12); // True
    }

    assert_eq!(x, 5);  // True

    let x = 42;
    println!("{}", x); // Prints "42".
}


// Unused Variables ------------------------------------------------------------------------
// Get rid of the warning
fn main() {
    let _x = 1;
}

#[allow(unused_variables)]
fn main() {
    let x = 1;
}


// Destructuring ------------------------------------------------------------------------

fn main() {
    let (x, y);
    (x,..) = (3, 4);
    [.., y] = [1, 2];
    assert_eq!([x,y], [3, 2]);
    println!("Success!");
} 




