import time
import random
import pyautogui
import keyboard

l = (
"american Express, amber moore, 348248269608986, 02/24, cid: 6191",
"american Express, melissa martinez, 348656350897237, 03/31, cid: 5441",
"american Express, ralph Lopez, 373729435225126, 12/29, cid: 2120",
"american Express, rhonda Holmes, 340579079176121, 11/24, cid: 2992",
"american Express, David Howard, 346496079032622, 11/26, cid: 3066",
"american Express, brittney bell, 378123353191756, 12/25, cid: 8767",
"american Express, Norma Greene, 346795522310570, 07/30, cid: 4960",
"american Express, Cody bullock, 379300226653167, 05/23, cid: 5072",
"american Express, Nicole Scott, 341960672721332, 08/26, cid: 6855",
"american Express, melissa Johnson, 373986503064627, 08/29, cid: 4150",
"american Express, melissa Hopkins, 348468597762178, 04/32, cid: 9047",
"american Express, william Haris, 347115326130570, 08/22, cid: 5724",
"american Express, Dana Smith, 377884093999128, 03/26, cid: 0521",
"american Express, andre Estes, 378879188418934, 02/23, cid: 0088",
"american Express, alison murphy, 372433791925376, 07/30, cid: 6037",
"american Express, Fernando Diaz, 340409279631131, 09/22, cid: 5083",
"american Express, Christine wilson, 346743352774440, 07/27, cid: 1878",
"american Express, John robinson, 371946835400404, 02/31, cid: 8895",
"american Express, maria Velasquez, 349365748373807, 02/32, cid: 5442",
"american Express, Lori andersen, 377490511375071, 09/31, cid: 0090",
"Diners Club / Carte Blanche, Thomas White, 30360143058859, 01/29, CVC: 115",
"VISA, Kenneth Moore, 4299603278124519, 02/24, CVC: 420",
"Diners Club / Carte Blanche, Christopher Patterson, 30482060027210, 06/26, CVC: 464",
"JCB, Joseph Short, 3513635941714070, 03/29, CVC: 275",
"VISA, Christopher Evans, 4695384506196989, 12/25, CVC: 743",
"VISA, Nicholas Olsen, 4538739447987773, 03/31, CVC: 978",
"Discover, Clifford Williams, 6521484162416773, 07/30, CVC: 974",
"VISA, Lindsay Smith, 4087729634157, 07/30, CVC: 724",
"VISA, Whitney Navarro, 4701577949752043, 10/22, CVC: 716",
"JCB, Kimberly Wise, 3518438610245335, 11/26, CVC: 318",
"Mastercard, Eric Walker, 5490790802473746, 04/30, CVV: 856",
"JCB, Kelly Pierce, 3548020332477059, 08/31, CVC: 331",
"Maestro, Dawn Jones, 676390456876, 11/28, CVV: 774",
"Maestro, Robert Huber, 060405718580, 10/23, CVV: 503",
"Diners Club / Carte Blanche, Jennifer Bailey, 30505407290552, 04/29, CVC: 687",
"JCB, Brad Hall, 213181811023366, 03/29, CVC: 665",
"Discover, Norma Thompson, 6588535156834436, 09/22, CVC: 737",
"VISA, Matthew Duncan, 4013270259871, 09/25, CVC: 735",
"Mastercard, Donna Whitaker, 5247755961333458, 03/26, CVV: 138",
"VISA, Lori Ingram, 4940100246060811, 01/25, CVC: 286",
"VISA, Doris Hall, 4127960941638566, 08/26, CVC: 742",
"VISA, David Acosta, 4384970632638, 01/31, CVC: 420",
"JCB, Dorothy Schultz, 3558862689701244, 04/32, CVC: 915",
"VISA, Zachary Spencer, 4155538949236362, 03/26, CVC: 747",
"VISA, Daniel Burgess, 4184366699788506, 04/23, CVC: 955",
"JCB, Jaime Lewis, 3508024174730524, 07/29, CVC: 162",
"Maestro, Ashley King, 501838284468, 09/28, CVV: 663",
"Mastercard, Jennifer Rojas, 2429271069458574, 10/27, CVV: 647",
"JCB, George Adams, 3515345411802441, 08/29, CVC: 546",
"VISA, John Johnson, 4307495559101, 12/30, CVC: 435",
"Mastercard, Jason Ortiz, 2267038804534075, 02/23, CVV: 723",
"VISA, Christopher Johnston, 4976211713443476, 08/25, CVC: 886",
"American Express, Seth Harrington, 370158056493263, 05/25, CID: 8455",
"Mastercard, Melissa Woods, 2265351910072282, 03/29, CVV: 082",
"Discover, Joseph Robinson, 6011495790890087, 03/32, CVC: 802",
"VISA, Mary Young, 4031580544402, 01/28, CVC: 227",
"Discover, Emily Carroll, 6523424305467778, 11/27, CVC: 936",
"JCB, Kimberly Brown, 213193871750598, 12/23, CVC: 611",
"VISA, Aaron Pearson, 4770719925775715, 02/29, CVC: 599",
"VISA, Victoria Holden, 4121852901362, 02/28, CVC: 572",
"American Express, Patricia Dillon, 345420472078165, 11/31, CID: 1841",
"VISA, Ryan Fuller, 4559599164406257651, 08/28, CVC: 761",
"VISA, Leah Brandt, 4630242469140600, 07/26, CVC: 665",
"American Express, Jesus Blake, 373974305264918, 09/25, CID: 6659",
"JCB, Michael Oconnor, 213157020211810, 07/30, CVC: 396",
"JCB, Shawn White, 3518228402193011, 03/29, CVC: 788",
"VISA, Larry Thomas, 4308371797692010130, 04/29, CVC: 001",
"Diners Club / Carte Blanche, Victoria Berger, 30354211648683, 03/32, CVC: 856",
"Maestro, Katherine Grant, 502004325580, 08/26, CVV: 018",
"VISA, Amy Clark, 4509670695945, 08/29, CVC: 126",
"VISA, Cindy Lyons, 4566786069415, 05/25, CVC: 082",
"Diners Club / Carte Blanche, Ronald Gonzalez, 30216360173211, 10/23, CVC: 907",
"Diners Club / Carte Blanche, Michael Wood, 30566019235252, 02/25, CVC: 838",
"JCB, Pam Williams, 3541082443842834, 01/28, CVC: 663",
"VISA, Carlos Wilcox, 4523566827897372, 07/27, CVC: 005",
"VISA, Stephanie Gross, 4179239608392107, 07/22, CVC: 776",
"American Express, Jonathan Lewis, 372069866336642, 08/22, CID: 2797",
"JCB, Elizabeth Navarro, 3578817621846719, 08/22, CVC: 514",
"JCB, Kevin Davis, 180086587694051, 11/23, CVC: 071",
"Mastercard, Joanna Oconnor, 2232218171181005, 06/29, CVV: 838",
"VISA, Courtney Medina, 4818180641349588, 07/22, CVC: 797",
"VISA, Robin Williams, 4673037766334, 06/24, CVC: 846",
"VISA, James Rice, 4032516481071593584, 07/24, CVC: 241",
"JCB, Steve Wagner, 180020413483462, 11/24, CVC: 477",
"Maestro, Sarah Golden, 502038942327, 01/28, CVV: 824",
"JCB, Michele Berger, 213161756332543, 01/23, CVC: 621",
"JCB, Frank Galvan, 3548159891588441, 03/29, CVC: 195",
"Maestro, Kevin Fletcher, 639089789015, 02/28, CVV: 994",
"Discover, Michael Hicks, 6011145348630598, 12/22, CVC: 990",
"Diners Club / Carte Blanche, Jeffrey Lopez, 30140205797556, 10/22, CVC: 030",
"Diners Club / Carte Blanche, Dennis Anderson, 38250849521833, 04/23, CVC: 706",
"Discover, Eric Mcknight, 6011344204157198, 07/22, CVC: 430",
"VISA, Kenneth Hopkins, 4611344241315859244, 12/23, CVC: 776",
"JCB, Alex Thompson, 3588643909198385, 01/27, CVC: 819",
"Discover, Laura Wright, 6535201293521717, 05/27, CVC: 521",
"American Express, Carla Simon, 340803593955103, 10/22, CID: 1276",
"JCB, Yvonne Pena, 3566070718302584, 03/31, CVC: 514",
"American Express, Micheal Mitchell, 379691067124635, 08/28, CID: 3724",
"VISA, Jeffrey Henry, 4912172906938063619, 02/27, CVC: 960",
"American Express, Karen Burton, 348488975977834, 12/29, CID: 9849",
"VISA, Jesse Clarke, 4471299888049459, 03/27, CVC: 331",
"Diners Club / Carte Blanche, Steven Banks, 30155830421026, 12/24, CVC: 374",
"VISA, Ariel Smith, 4935134099705625, 02/29, CVC: 184",
"VISA, Steve Baker, 4727852167915659, 07/28, CVC: 485",
"VISA, Brent Perez, 4298276193045174543, 12/23, CVC: 937",
"VISA, Jessica Briggs, 4550959465708736, 06/24, CVC: 223",
"VISA, Ronald Cabrera, 4438681455747306959, 05/29, CVC: 410",
"VISA, Daryl Shields, 4675473771645, 11/29, CVC: 565",
"Discover, Jonathan Black, 6011279486426467, 11/22, CVC: 183",
"JCB, Monique Weaver, 180036402601237, 10/30, CVC: 189",
"VISA, Kelsey Ford, 4761918356792680365, 04/30, CVC: 635",
"JCB, Joshua Bowers, 213168605020732, 11/31, CVC: 132",
"Maestro, Anna Burke, 675974518705, 03/24, CVV: 956",
"Maestro, Robert Wells, 675927542422, 11/22, CVV: 083",
"VISA, Dawn Collins, 4846791984406, 12/29, CVC: 227",
"JCB, Valerie Bell, 3510636009909084, 02/23, CVC: 789",
"Mastercard, Lori Chapman, 2720660556281919, 12/31, CVV: 673",
"VISA, Bethany Parks, 4043758641688, 02/26, CVC: 810",
"Discover, Shawn Reeves, 6011855395013478, 01/24, CVC: 790",
"VISA, Kevin Brown, 4933757794040310, 11/26, CVC: 898"
)
time.sleep(60)
while True:
    send = random.choice(l)
    print(send.lower())
    for letter in send:
        if letter != "'":
            keyboard.send(letter.lower())
        else:
            continue
    pyautogui.moveTo(1165,548)
    pyautogui.click(1165,548)
    time.sleep(2)
