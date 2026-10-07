"""All content for the West Point Scavenger Hunt.

Edit stops here, then run build.py to regenerate the web page and PDFs.
Coordinates marked CHECK are estimates that still need a pin check on site.
"""

TITLE = "West Point Scavenger Hunt"
EDITION = "2026 Edition"

START = {
    "id": "ike_hall",
    "name": "Eisenhower Hall",
    "lat": 41.39587, "lng": -73.96006,
    "intro": "Welcome, cadets! Your mission: follow the clues across West Point. "
             "At each stop, do the activity, answer the challenge, and learn something new. "
             "Grown-ups: tap the map links or scan the QR code to get walking directions.",
}

STOPS = {
    "cannons": {
        "name": "Cannons by the Firstie Club",
        "lat": 41.39498, "lng": -73.95858,  # CHECK: First Class Club building center
        "clue": [
            "Up the hill where the oldest cadets go to chill,",
            "big iron friends sit perfectly still.",
            "They used to go BOOM, now they just stay.",
            "Find the cannons and pick your favorite today!",
        ],
        "walk": {"ike_hall": "Head up the hill to the east from Eisenhower Hall toward the First Class Club. The cannons are on the lawn nearby."},
        "activity": "Find the compass near the cannons. Which direction do the cannons point? Everybody point that way and shout it out! Then count the cannons and pick the biggest and the smallest.",
        "question": "What is a “Firstie”?",
        "answer": "A senior! West Point seniors are called First Class cadets, or “Firsties.” The First Class Club is their hangout.",
        "facts": [
            "West Point has its own names for each class year: freshmen are Plebes, sophomores are Yearlings, juniors are Cows, and seniors are Firsties.",
            "Juniors are called “Cows” because long ago they finally got to go home on leave after two years away, “when the cows come home.”",
            "Captured cannons have been displayed at West Point since the Revolutionary War. The first ones were taken from the British at the Battles of Saratoga in 1777.",
        ],
    },
    "tunnel": {
        "name": "Beat Navy Tunnel",
        "lat": 41.394077, "lng": -73.958906,
        "clue": [
            "Army's big rival sails out on the sea.",
            "Go under the road for a cheer, one, two, three!",
            "Every Army win is painted on the wall.",
            "Find the tunnel and give it your loudest call!",
        ],
        "walk": {"cannons": "From the cannons, take the path south. It dips down and goes under Washington Road through the tunnel."},
        "activity": "Count how many years are painted on the walls. Then everybody yell “BEAT NAVY!” at the same time and listen for the echo.",
        "question": "In what year did Army and Navy play their very first football game?",
        "answer": "1890, right here at West Point. Navy won that first game, so Army has been trying to beat Navy ever since!",
        "facts": [
            "The Army–Navy Game is one of the oldest rivalries in college football. It is played every December.",
            "During the week before the game, cadets everywhere say “Beat Navy!” instead of hello.",
            "Army, Navy, and Air Force compete for the Commander-in-Chief's Trophy. The President presents it to the winner.",
        ],
    },
    "thayer": {
        "name": "Sylvanus Thayer Statue",
        "lat": 41.39374, "lng": -73.95893,
        "clue": [
            "Who made cadets do homework BEFORE class each day?",
            "The Father of West Point, who still stands here today.",
            "Pop out of the tunnel and climb up the stair.",
            "A man made of bronze is waiting right there!",
        ],
        "walk": {"tunnel": "Come out of the tunnel and up the stairs. Thayer's statue is just ahead, across from the Commandant's house."},
        "activity": "Count the buttons on Colonel Thayer's coat. Then try the Thayer Method: each kid teaches everyone else one thing they learned today.",
        "question": "Thayer already had a college degree when he came to West Point. How long did it take him to graduate?",
        "answer": "About one year! He graduated from Dartmouth College in 1807, then from West Point in 1808.",
        "facts": [
            "Thayer was Superintendent (the boss of West Point) from 1817 to 1833. He is called the “Father of the Military Academy.”",
            "His idea was for cadets to study before class, then solve problems at the chalkboard in small groups. West Point still teaches this way, and it's called the Thayer Method.",
            "West Point was the first engineering school in America. Its graduates helped build many of the country's early roads, bridges, and railroads.",
            "Every year at graduation, the oldest living West Point graduate lays a wreath at this statue.",
        ],
    },
    "macarthur": {
        "name": "Douglas MacArthur Monument",
        "lat": 41.39278, "lng": -73.9588,
        "clue": [
            "A five-star general who loved a corncob pipe,",
            "gave a famous speech, and it wasn't just hype.",
            "Head to the barracks that carry his name.",
            "Stone walls nearby are carved with his fame!",
        ],
        "walk": {"thayer": "Walk south on the path toward the big stone barracks. The statue and its plaza are at the north end of MacArthur Barracks, across the street from the Superintendent's house."},
        "activity": "Who can pose exactly like MacArthur? Take a photo of everyone doing their best MacArthur. Then race to find the words “Duty, Honor, Country” carved in the stone walls.",
        "question": "What three words are West Point's motto?",
        "answer": "Duty, Honor, Country. They're carved right here, from MacArthur's famous 1962 speech to the cadets.",
        "facts": [
            "MacArthur graduated first in his class in 1903. Later he came back to be West Point's Superintendent.",
            "He and his father, Arthur MacArthur, both earned the Medal of Honor. They were the first father and son to do it.",
            "He was a five-star General of the Army. That's the highest rank there is, and only five Army generals have ever held it.",
            "His wife, Jean, dedicated this statue in 1969.",
        ],
    },
    "chapel": {
        "name": "Cadet Chapel",
        "lat": 41.39029, "lng": -73.9599,
        "clue": [
            "Look up, way up, to the castle on the hill,",
            "with a giant pipe organ and bells that ring still.",
            "Climb the steps, all of them, high over the Plain.",
            "Your legs will complain, but your eyes will gain!",
        ],
        "walk": {"macarthur": "The chapel is the castle-like building on the hill behind the barracks. Follow the road and stairs uphill. It's steep, so take your time."},
        "activity": "Count the steps on the way up. At the top, turn around: who can find the Plain? The Hudson River? The tall Battle Monument column? If the doors are open, peek inside and look up.",
        "question": "About how many pipes does the chapel's organ have?",
        "answer": "More than 23,000! It's one of the largest pipe organs in any church in the world. It started with about 2,400 pipes in 1911 and kept growing.",
        "facts": [
            "The Cadet Chapel was finished in 1910. It's built in the Gothic style, like a medieval castle or cathedral.",
            "The bell tower holds twelve bells that weigh more than 14,000 pounds together. Cadets still ring them by hand.",
            "Many of the stained-glass windows were gifts from graduating classes.",
        ],
    },
    "washington": {
        "name": "George Washington Statue",
        "lat": 41.39201, "lng": -73.95775,
        "clue": [
            "First in war, first in peace, and first on the dollar bill.",
            "He's sitting on his horse and holding very still.",
            "Out in front of the hall where cadets sit down to eat,",
            "find the general whose horse never moves its feet.",
        ],
        "walk": {"chapel": "Head back down the hill to Washington Hall, the huge building at the south end of the Plain. Washington on horseback is out front."},
        "activity": "Look at the horse's legs. How many hooves are touching the ground? Then everyone give George your best salute.",
        "question": "Which general tried to hand West Point over to the British?",
        "answer": "Benedict Arnold, in 1780. He was West Point's commander! The plot failed when the British spy John André was caught with the plans hidden in his boot.",
        "facts": [
            "Washington said West Point was the most important post in America. Whoever held it controlled the Hudson River.",
            "Washington Hall behind the statue is the cadet dining hall. All of the roughly 4,400 cadets eat lunch there at the same time.",
            "This statue was dedicated in 1916. It's a copy of a famous statue of Washington in Union Square, New York City.",
        ],
    },
    "eisenhower": {
        "name": "Ike, Patton & the Library",
        "lat": 41.39187, "lng": -73.95637,
        "clue": [
            "He led D-Day, then was President too.",
            "Everyone called him \u201cIke.\u201d Wouldn't you?",
            "Walk along the Plain to the library tall.",
            "Two famous generals are waiting for you all!",
        ],
        "walk": {"washington": "Walk east along the south edge of the Plain. Ike stands near the corner of the Plain by the library, and Patton is close by."},
        "activity": "Take a photo with Ike. Then find General Patton nearby and look closely: what is he holding? Use your hands as pretend binoculars and scan the Plain like Patton. Last, find the name on the library building. Whose hall is it?",
        "question": "What year did Eisenhower graduate from West Point?",
        "answer": "1915. His class is called \u201cthe class the stars fell on\u201d because 59 of its 164 graduates became generals.",
        "facts": [
            "Ike played football for Army. In 1912 he even played against Jim Thorpe, one of the greatest athletes ever. A knee injury ended his playing, so he became a cheerleader and coach.",
            "In World War II he was Supreme Allied Commander and led the D-Day invasion on June 6, 1944. Later he was the 34th President of the United States.",
            "General Patton took five years to graduate instead of four because he had to repeat his first year. Math was hard for him!",
            "Cadets joke that Patton's statue stands by the library so he could finally find it.",
            "The library is called Jefferson Hall, after Thomas Jefferson. He signed the law that started West Point on March 16, 1802.",
        ],
    },
    "doubleday": {
        "name": "Doubleday Field",
        "lat": 41.3925, "lng": -73.9553,  # CHECK: west edge of the field
        "clue": [
            "Peanuts, Cracker Jacks, and a diamond of green.",
            "Its “inventor” was a cadet, or so it would seem.",
            "Follow the edge of the Plain to the field with a backstop wall.",
            "Batter up, Black Knights! Let's play ball!",
        ],
        "walk": {"eisenhower": "Keep heading east from Ike and Patton. The baseball field is on the east side of the Plain."},
        "activity": "Open the compass on a phone. If you hit a home run right over the pitcher's head, which direction would the ball fly? Then everyone take your best home-run swing and run the bases in place.",
        "question": "Did Abner Doubleday really invent baseball?",
        "answer": "Probably not! A 1907 committee gave him the credit, but historians say baseball grew out of older games like rounders. In 1839, the year he supposedly invented it, he was a cadet here at West Point.",
        "facts": [
            "Abner Doubleday graduated from West Point in 1842.",
            "At the start of the Civil War he aimed the first Union cannon shot in defense of Fort Sumter.",
            "Army's baseball team plays here, with the Hudson River just beyond the outfield.",
        ],
    },
    "supes_box": {
        "name": "The Superintendent's Review Box",
        "lat": 41.39341, "lng": -73.9562,
        "clue": [
            "Who has the best seat when the cadets march by?",
            "The Superintendent! Go find those stands nearby.",
            "Look across the Plain, all grassy and wide.",
            "Barracks and a giant mess hall line every side!",
        ],
        "walk": {"doubleday": "Walk north along the east edge of the Plain. The Review Box is the set of stands facing the parade field."},
        "activity": "Look across the Plain to Washington Hall in the middle and the barracks on each side. If you lived on the top floor, how many flights of stairs would you climb? Then march 20 steps together in a parade: left, right, left!",
        "question": "Spot the sports field to the north with H-shaped posts. Which sport is it for?",
        "answer": "Rugby! Rugby goals are H-shaped. That's Daly Field, where Army also plays lacrosse.",
        "facts": [
            "The Plain is West Point's parade field. Soldiers of the Continental Army drilled and camped here during the Revolutionary War.",
            "A parade where a leader watches the cadets march past is called a “review.”",
            "The Superintendent is the head of West Point. The job is held by a three-star general.",
            "The whole Corps of Cadets, about 4,400 people, can march onto the Plain together.",
        ],
    },
    "sedgwick": {
        "name": "Sedgwick's Lucky Spurs",
        "lat": 41.39447, "lng": -73.95661,
        "clue": [
            "Need a little luck before a big test?",
            "Spin a general's spurs. Cadets say it works best!",
            "Follow the Plain's edge to where “Uncle John” stands,",
            "and give his boot wheels a spin with your hands.",
        ],
        "walk": {
            "macarthur": "Walk east along the north edge of the Plain, past the Superintendent's house, toward Trophy Point. Sedgwick stands near Washington Road.",
            "grant": "Sedgwick is just a few steps away, near Washington Road, across from the tall Battle Monument.",
        },
        "activity": "Find the spurs on Sedgwick's boots. Do they really spin? Give them a gentle spin and make a wish for your next test.",
        "question": "Why do cadets spin Sedgwick's spurs?",
        "answer": "For luck! Legend says a cadet about to fail should spin the spurs at midnight before the final exam, wearing full dress uniform, and they'll pass.",
        "facts": [
            "General John Sedgwick's soldiers loved him so much they called him “Uncle John.” They paid for this statue themselves in 1868.",
            "He was the highest-ranking Union officer killed in the Civil War, at the Battle of Spotsylvania in 1864.",
            "In 2024 the statue was cleaned and the spurs were repaired so they would keep spinning, a gift from the West Point Class of 1978.",
        ],
    },
    "grant": {
        "name": "Ulysses S. Grant Statue",
        "lat": 41.3942, "lng": -73.9562,  # CHECK: corner of the Plain by Thayer Road, across from Battle Monument
        "clue": [
            "His real name was Hiram, but a mix-up, oh my,",
            "made him \u201cU.S. Grant,\u201d so friends called him \u201cSam.\u201d That's why!",
            "He won the Civil War, then was President too.",
            "The Plain's newest statue is waiting for you!",
        ],
        "walk": {
            "sedgwick": "Grant stands a few steps away at the corner of the Plain near Thayer Road, across from Battle Monument.",
            "supes_box": "Walk north along the edge of the Plain toward Battle Monument. Grant stands at the corner near Thayer Road.",
        },
        "activity": "Grant is holding two things. What are they? Then, out on the grass, everyone gallop like a horse and leap over a pretend high-jump bar.",
        "question": "Grant was the best horse rider in his class. What record did he set as a cadet?",
        "answer": "A high-jump record on his horse, York. It lasted about 25 years!",
        "facts": [
            "Grant was born Hiram Ulysses Grant. The congressman who sent him to West Point wrote his name as \u201cUlysses S. Grant\u201d by mistake, and the name stuck.",
            "Because his initials were U.S., his classmates nicknamed him \u201cUncle Sam,\u201d or just \u201cSam.\u201d",
            "He graduated in 1843 and became the first West Point graduate to be President of the United States.",
            "This statue was added in 2019. He's holding riding gloves, a nod to his horse skills, and a sword.",
        ],
    },
    "battle": {
        "name": "Battle Monument & the Hidden Prize",
        "lat": 41.3947, "lng": -73.95683,
        "clue": [
            "A super-tall column as smooth as can be,",
            "with a winged lady on top for all to see.",
            "Big stone balls and old cannons stand guard on the ground.",
            "Peek inside the cannons. Is there treasure to be found?",
        ],
        "walk": {
            "overlook": "Climb back up from the overlook and walk west across Trophy Point to the tall column.",
            "chain": "Walk back west across Trophy Point to the tall column.",
        },
        "activity": "Peek inside the cannons around the monument. Did somebody leave a prize? Then take a picture with the big granite balls. Can your family link arms all the way around one? Look up: who can see the statue on the very top?",
        "question": "The statue on top is named after a word that means being very well known. What's her name?",
        "answer": "Fame! She was sculpted by Frederick MacMonnies.",
        "facts": [
            "The column is 46 feet tall and made of one polished piece of granite. It's believed to be one of the largest polished granite columns in the Western Hemisphere.",
            "It honors the 2,230 Regular Army soldiers and officers who died for the Union in the Civil War. Their names are carved here.",
            "Soldiers paid for it by giving a little bit of their pay. It was dedicated in 1897.",
        ],
        "grownup_tip": "Want a prize moment? Before you start, hide a small treat in the mouth of one of the cannons here and tell the kids to check inside.",
    },
    "chain": {
        "name": "The Great Chain",
        "lat": 41.39557, "lng": -73.95569,
        "clue": [
            "To stop British ships from sailing upriver,",
            "they stretched something across that would make captains shiver.",
            "Each link weighs as much as a grown-up, maybe more!",
            "Find the giant chain near the river's shore.",
        ],
        "walk": {
            "battle": "Head northeast across Trophy Point toward the river. The chain links are on the east end.",
            "sedgwick": "Cross Washington Road carefully and head northeast across Trophy Point toward the river. The chain links are on the east end.",
            "grant": "Cross the road carefully and head northeast across Trophy Point toward the river. The chain links are on the east end.",
        },
        "activity": "Measure one link with your hands. How many hands long is it? Then lie down next to the chain: how many kids long is the whole thing?",
        "question": "The chain was made of heavy iron. How did it stay on top of the water?",
        "answer": "It was attached to big floating logs, like rafts, all the way across the river.",
        "facts": [
            "In 1778, soldiers stretched the Great Chain across the Hudson River from West Point to Constitution Island. That's the island you can see across the water.",
            "Each link is about 2 feet long and weighs over 100 pounds. The whole chain was about a third of a mile long.",
            "It was taken out every winter so the river ice wouldn't wreck it, then put back every spring.",
            "The British never tried to break through it.",
        ],
    },
    "overlook": {
        "name": "Hudson River Overlook",
        "lat": 41.3962, "lng": -73.9555,  # CHECK: overlook below the Great Chain
        "clue": [
            "Barges and tugboats and sailboats too",
            "chug up the Hudson. How many can you view?",
            "Just below the chain there's a spot by the rail.",
            "Be the lookout and spot a boat or a sail!",
        ],
        "walk": {"chain": "Just below the chain is a small overlook by the railing. Hold hands, because there's a drop-off."},
        "activity": "Be the lookout! Count every boat you can see. Which way is each one going? Look at the water too: is it flowing left or right right now?",
        "question": "Which way does the Hudson River flow?",
        "answer": "Both ways! The ocean's tides push all the way up past West Point, so the water flows north for a few hours, then south. A Native American name for the river means “the river that flows both ways.”",
        "facts": [
            "The water near West Point is the deepest part of the Hudson, about 200 feet deep. Sailors called it “World's End” because of its tricky winds and currents.",
            "The river makes a sharp S-shaped bend here. Old sailing ships had to slow down to turn, which made them easy targets for cannons. That's why West Point was so important.",
        ],
    },
    "finale": {
        "name": "The Million-Dollar View",
        "lat": 41.3952, "lng": -73.9571,  # CHECK: view spot above the amphitheater
        "clue": [
            "You made it to the end, and the view is the prize!",
            "Find the big grassy hill that will open your eyes.",
            "Look north up the river past mountains so grand.",
            "It's the million-dollar view, the best in the land!",
        ],
        "walk": {
            "battle": "From Battle Monument, walk to the top of the grassy hill and look north up the river.",
        },
        "activity": "BONUS ROUND! (1) Take a drink from the water fountain below Battle Monument. (2) Roll or run down the hill, but be careful, it's steeper than it looks! (3) Take a family photo with the million-dollar view. Last of all, everyone shares their favorite stop.",
        "question": "Looking up the river, what is the big mountain on the left?",
        "answer": "Storm King Mountain. Across the river on the right is Breakneck Ridge.",
        "facts": [
            "Trophy Point is named for the captured cannons, or “trophies,” displayed here. They come from five different wars.",
            "Painters from the Hudson River School, a famous group of American artists in the 1800s, came here to paint this view.",
            "In the summer, the West Point Band plays concerts in the amphitheater below the hill.",
        ],
    },
}

ROUTES = {
    "short": {
        "name": "Short Route",
        "tagline": "Tunnel, statues, the Great Chain, a hidden prize, and the big view.",
        "stops": ["cannons", "tunnel", "thayer", "macarthur", "sedgwick", "grant", "chain", "battle", "finale"],
        "terrain": "Mostly flat sidewalks and paths. The tunnel has a short set of stairs.",
    },
    "long": {
        "name": "Long Route",
        "tagline": "Everything on the short route, plus the Cadet Chapel, Washington, Ike and Patton, and a loop around the Plain.",
        "stops": ["cannons", "tunnel", "thayer", "macarthur", "chapel", "washington", "eisenhower",
                  "doubleday", "supes_box", "grant", "sedgwick", "chain", "overlook", "battle", "finale"],
        "terrain": "Includes a steep climb with stairs up to the Cadet Chapel. Strollers will struggle on that stretch. Everything else is sidewalks and paths.",
    },
}

ADULT_NOTES = [
    "West Point is an active Army post. Check the current visitor access rules on westpoint.edu before you go, and bring photo ID for every adult. Please keep voices down near barracks and academic buildings when classes are in session. Park at Eisenhower Hall. Both routes end at Trophy Point, a short walk back to the car.",
    "Bring a phone with a compass app, water, and something to write with.",
]

# Password check shown before the hunt opens. One question is picked at random.
# Only SHA-256 hashes of the answers are stored (this repo is public). To set a new answer:
#   python3 -c "import hashlib; print(hashlib.sha256(b'1234').hexdigest())"
# Answers are digits only; the page strips commas and spaces before checking.
GATE = [
    {"q": "How many names are on Battle Monument?", "h": "903a4207be29cb52c7c28b6b3e83b7bea776a390167924fe8ff18aa325f10285"},
    {"q": "How many million gallons of water are in Lusk Reservoir when water is flowing over the spillway?", "h": "349c41201b62db851192665c504b350ff98c6b45fb62a8a2161f78b6534d8de9"},
    {"q": "How many lights are in Cullum Hall?", "h": "9644294ac4ffb3091eef01219b3fe4fe467f05890cc56af961dce68fddbb7704"},
]


def gmaps(lat, lng):
    return f"https://www.google.com/maps/dir/?api=1&destination={lat},{lng}&travelmode=walking"


def amaps(lat, lng):
    return f"https://maps.apple.com/?daddr={lat},{lng}&dirflg=w"
