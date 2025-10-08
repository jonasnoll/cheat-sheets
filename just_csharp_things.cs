// VARIABLES ---------------------------------------------------------------------------

int myNum = 0;
string currString = "Hi there!";
var inferredVariable = 12;
bool hasDoneC = false;

string combinedString = "Cool oder - " + currString;

Console.WriteLine(currString);
Console.WriteLine(hasDoneC);
Console.WriteLine(myNum);
Console.WriteLine(inferredVariable);
Console.WriteLine(combinedString);

Console.WriteLine($"{currString} How are you?");
Console.WriteLine();

// ARRAYS ---------------------------------------------------------------------------
// Not common at all in csharp
string[] favRats = ["fancy rat", "brown rat", "red rat", "big rat"];
favRats[0] = "super fancy rat";
// LINQ
var newFavRats = favRats.Where(x => x.StartsWith("b"));

foreach (var rat in newFavRats)
{
    Console.WriteLine(rat);
}
Console.WriteLine();

// LOOPS ---------------------------------------------------------------------------
// For Loofs 
for (var i = 0; i < 10; i++)
{
    Console.WriteLine(i + 1);
}
// for each
foreach (var rat in newFavRats)
{
    Console.WriteLine(rat);
}
// LINQ
newFavRats.ToList().ForEach(x => Console.WriteLine(x));

// IF ---------------------------------------------------------------------------
bool isLoggedIn = false;
bool isAdmin = false;
if (isLoggedIn)
{
    Console.WriteLine("Yup is true");
}
else if (isAdmin)
{
    Console.WriteLine("is admin");
}
// else if (inferredVariable is String)
// {
//     Console.WriteLine("String");
// }
else
{
    Console.WriteLine("not admin and not logged in");
}

// FUNCTIONS ---------------------------------------------------------------------------
var getName = (int x) =>
{
    return $"hi {x}";
};

// ENUM ---------------------------------------------------------------------------
// enum Level 
// {
//   Low,
//   Medium,
//   High
// };

// Level myVar = Level.Medium;
// Console.WriteLine(myVar);

// SWITCH ---------------------------------------------------------------------------
var myFish = "Makrele";

var result = myFish switch
{
    "Makrele" => "Yes!",
    "Cobbler" => "Buuuhhh!",
    _ => "Nice"
};
Console.WriteLine(result);


// CLASSES ---------------------------------------------------------------------------
Rat wolfRat = new Rat(); // new() würde auch reichen

wolfRat.Number = 1;
wolfRat.Name = "Joe";
wolfRat.IsRadioActive = true;

Console.WriteLine(wolfRat.FightPickleRick());

// TOUPLES ---------------------------------------------------------------------------
var valz = ("a", 5, "c");
Console.WriteLine(valz.Item1);

var valzWithName = (a: "a", b: 5, c: "c");
Console.WriteLine(valzWithName.a);

// Static Class Methods
Console.WriteLine(TimeUtility.GetCurrentTime());

// LISTS ---------------------------------------------------------------------------
List<string> listStr = ["a", "b", "c", "d", "e"];
List<int> listNum = [1, 2, 3, 4];

var a = listNum[0];
// update
listNum.Add(5);
// read
foreach (var item in listNum)
{
    Console.WriteLine(item);
}

var newNums = listNum.Where(x => x != 2);
foreach (var item in newNums)
{
    Console.WriteLine(item);
}

// RECORDS ---------------------------------------------------------------------------
// Immutable classes
// Muss nicht unbedingt sein...

// Type Safe Function Pointer


// Callback ---------------------------------------------------------------------------
var callCall = (Action myFunc) => myFunc();


// Dictionaries ------------------------
Dictionary<string, int> myDict = new();

// Hash Set
HashSet<string> mySet = new();






