import re

response_text = """
Found records for Allan Sadun:
41752|04SAN2795001|SADUN|ALLAN|ELVIO||237||ELM ST|1|021391476|237 ELM ST|1|CAMBRIDGE|MA|021391476|D |04/27/1995|10/17/2017|03|02|8|1311|143|A

No records found for Dan Eisner.
Found records for Marc McGovern:
26724|12MMK2168000|MCGOVERN|MARC|C||17||PLEASANT ST||02139||||||D |12/21/1968|09/30/1994|04|02|6|1311|142|A

No records found for Christopher Schmidt.
No records found for Jessica Schmidt.
Found records for Pamela Thilo:
28363|11TPA1470001|THILO|PAMELA|B||65||MARTIN ST||02138||||||D |11/14/1970|10/12/1994|08|01|6|34|142|A

No records found for Eugenia Huh.
No records found for Jess Sheehan.
Found records for Nory Klop-Packel:
50165|10KNY3000000|KLOP-PACKEL|NORY|GRAY||129||FRANKLIN ST|107|021394100|129 FRANKLIN ST|107|CAMBRIDGE|MA|021394100|D |10/30/2000|10/15/2018|05|01|8|1311|143|A

Found records for Dana Bein:
35699|07BDA1778004|BEIN|DANA|JAY||173||HAMPSHIRE ST|4|021391336||||||D |07/17/1978|07/09/2004|03|02|8|1311|143|A

Found records for Ming-Tai Huh:
22258|05HMA0480000|HUH|MING-TAI|||259||WASHINGTON ST||021393503||||||D |05/04/1980|10/17/2006|03|03|8|1311|143|A

No records found for Nick Jordan.
Found records for Steven Ngo:
50099|09NSN0200000|NGO|STEVEN|||124||BERKSHIRE ST|5|02141||||||U |09/02/2000|08/10/2022|02|01|8|1311|143|A

Found records for Camilla Elvis:
52416|02ECA1790001|ELVIS|CAMILLA|JANE FABBIANO||28||LINNAEAN ST||021381611|28 LINNAEAN ST||CAMBRIDGE|MA|021381611|D |02/17/1990|06/25/2008|08|01|6|34|142|A

Found records for Nathan Klima:
45195|01KNN2297000|KLIMA|NATHAN|LAWRENCE||34||ROCKINGHAM ST||02139||||||D |01/22/1997|01/08/2020|05|03|8|1311|143|A

No records found for Michael Silver.
Found records for Joe McGuirk:
23319|04MJH1865001|MCGUIRK|JOE|||314||COLUMBIA ST|1|021411310|314 COLUMBIA ST|1|CAMBRIDGE|MA|02141|D |04/18/1965|03/05/2010|02|01|8|1311|143|A

No records found for Daniel Kant.
No records found for Anthony David.
Found records for Michael Monestime:
35910|10MML2578000|MONESTIME|MICHAEL|SCOTT||4||GEORGE ST||021401717|4 GEORGE ST||CAMBRIDGE|MA|021401717|D |10/25/1978|09/17/2002|11|03A|8|34|146|A

No records found for Lukas Drexler-Bruce.
No records found for Nina DeAgrela.
No records found for Mollie Wilkinson.
No records found for Dana Osei.
No records found for Tiwalayo Aina.
No records found for Enrique Montas.
No records found for Dana McCormack.
No records found for Ness Vera.
No records found for Emily Sullivan.
No records found for Amira Malik.
Found records for Mark Mulgay:
19728|12MMK1060002|MULGAY|MARK|H||1558||MASSACHUSETTS AVE|2|02138|205 MOUNT AUBURN ST|1D|CAMBRIDGE|MA|02138|D |12/10/1960|10/06/2016|07|02|6|1311|142|A

No records found for Niko Emack.
No records found for Shreya Thipireddy.
Found records for Melody Wu:
67663|08WMY2501000|WU|MELODY|||471||MEMORIAL DR||021394319||||||U |08/25/2001|09/03/2019|05|02|8|1311|201|I

No records found for Deb Nicholson.
Found records for Kathleen Moore:
17125|07MKN3058000|MOORE|KATHLEEN|S||9||DOANE ST||021384727|9 DOANE ST||CAMBRIDGE|MA|021384727|D |07/30/1958|09/30/1992|09|01|6|1332|146|A

No records found for Harveer Singh.
Found records for Jack Lewis:
45209|01LJK3097000|LEWIS|JACK|||44||CLAY ST|2|021402645||||||D |01/30/1997|09/28/2021|11|01A|8|34|146|A

55867|09LJK1092000|LEWIS|JACK|S||5||GLASSWORKS AVE|358|021414116||||||D |09/10/1992|08/31/2020|01|01|8|1311|185|A

No records found for Liliana Edmonds.
No records found for Eilzeabth Baidlwn.
No records found for Zoe Wu.
No records found for Andy Tockman.
No records found for Ken Cox.
No records found for Christina Antonakakis.
No records found for Tomás Herrera.
No records found for B. Kimmerman.
No records found for Ayesha Ali.
No records found for Emily Tess.
No records found for Kidist Adamu.
No records found for Kristin Sheridan.
Found records for Ayodeji Lindblad:
50563|06LAI0401000|LINDBLAD|AYODEJI|||290||MASSACHUSETTS AVE||021394958||||||D |06/04/2001|02/06/2020|03|03|8|1311|143|A

No records found for Haniya Shareef.
No records found for Alexis Yang.
No records found for Alex Lopez.
Found records for Michael Mazumder:
67132|10MML0500000|MAZUMDER|MICHAEL|||305||MEMORIAL DR||02139|305 MEMORIAL DR|0064|CAMBRIDGE|MA|02139|D |10/05/2000|02/12/2020|01|02|8|1311|185|A

Found records for Theresa Caso-McHugh:
67163|10CTA2400000|CASO-MCHUGH|THERESA|C||3||AMES ST||02142|3 AMES ST|203|CAMBRIDGE|MA|021421367|U |10/24/2000|06/28/2021|01|02|8|1311|185|A

No records found for John Monterey.
Found records for Frantz Pierre:
24016|09PFZ2682000|PIERRE|FRANTZ|||22||WATER ST||021411257|22 WATER ST||CAMBRIDGE|MA|021411257|D |09/26/1982|06/21/2003|01|03|8|1311|143|A

No records found for Tony Pini.
No records found for Gatlen Culp.
Found records for Christopher Lim:
32664|07LCR2075001|LIM|CHRISTOPHER|YITSEONG||48||PLEASANT ST||021393838|48 PLEASANT ST||CAMBRIDGE|MA|021393838|D |07/20/1975|07/18/2006|04|03|8|1311|142|A

Found records for Risa Mednick:
22855|09MRA1964000|MEDNICK|RISA|||20||MAPLE AVE|C|021391129||||||D |09/19/1964|10/20/1999|06|01A|6|1311|143|A

Found records for Nick Ortiz:
34753|10ONK0791000|ORTIZ|NICK|F||820||MASSACHUSETTS AVE|208|021393228|820 MASSACHUSETTS AVE|208|CAMBRIDGE|MA|021393228|U |10/07/1991|01/27/2023|04|02|6|1311|142|A

No records found for Soy Choi.
Found records for Grace Tang:
67630|08TGE0301000|TANG|GRACE|WEN-LIAN||500||MEMORIAL DR||02139||||||D |08/03/2001|10/16/2019|05|02|8|1311|201|A

Found records for Matthew Morris:
55703|05MMW2292001|MORRIS|MATTHEW|EDWARD||1105||MASSACHUSETTS AVE|10C|02138||||||D |05/22/1992|10/17/2018|06|02|6|1311|142|I

No records found for Mufaro Makiwa.
No records found for Jesus Crespo.
No records found for Blake Shepherd.
Found records for Eren Shin:
50555|05SEN2501003|SHIN|EREN|||30||NORFOLK ST|3|02139|30 NORFOLK ST|3|CAMBRIDGE|MA|02139|U |05/25/2001|06/10/2022|05|01|8|1311|143|A

No records found for Subha Pushpita.
No records found for Bilal Daqqah.
No records found for Johnvir Pangli.
No records found for Barış Ekim.
No records found for Aljazzy Alahmadi.
Found records for Grace Mao:
58333|04MGE0694000|MAO|GRACE|||1||GRAY ST|7|021381559||||||D |04/06/1994|07/24/2017|08|01|6|34|142|I

No records found for Thomas Asard.
No records found for Prajwal Mahesh.
No records found for Katie Williams.
No records found for Jess Cohen.
No records found for Tim Gutterman.
Found records for Victor Perez-Ramirez:
66931|06PVR2500000|PEREZ-RAMIREZ|VICTOR|M||471||MEMORIAL DR||021394319||||||U |06/25/2000|10/17/2018|05|02|8|1311|201|A

Found records for Uyen Nguyen:
58233|03NUN1494000|NGUYEN|UYEN|PHUONG||17||BRISTOL ST|1|021411997||||||U |03/14/1994|06/18/2020|02|01|8|1311|143|I

No records found for Jordan Barton.
No records found for Alana Kalehua.
No records found for Carlos Mercado-Lara.
No records found for Alex Ellison.
No records found for Nikasha Patel.
Found records for Gretchen Eggers:
41488|03EGN0695001|EGGERS|GRETCHEN|||190||3RD ST|2|02141||||||D |03/06/1995|09/30/2016|02|03A|8|1311|143|I

Found records for Olivia Siegel:
64009|11SOA1697000|SIEGEL|OLIVIA|CAROLINA||410||MEMORIAL DR||02139||||||D |11/16/1997|10/07/2016|01|02A|8|1311|201|I

No records found for Isaac Toscano.
No records found for Ariana Adames.
No records found for Keith Skaggs.
Found records for Deniz Sert:
67268|12SDZ2300000|SERT|DENIZ|B||362||MEMORIAL DR||021394071|362 MEMORIAL DR|406|CAMBRIDGE|MA|02139|R |12/23/2000|09/25/2019|01|02|8|1311|185|A

No records found for Park Suckerberg.
No records found for Kristina Chen.
Found records for Elisabeth Bullock:
66359|11BEH0499000|BULLOCK|ELISABETH|D||229||VASSAR ST||021394310||||||U |11/04/1999|10/17/2018|05|02|8|1311|201|A

Found records for Thomas Adebiyi:
48375|02ATS0599000|ADEBIYI|THOMAS|O||5||MARCELLA ST||02141||||||U |02/05/1999|02/05/1999|02|01|8|1311|143|I

No records found for Blair Anaman-Williams.
No records found for Keshav Gupta.
No records found for Yueyang Fan.
No records found for Devin Seyler.
No records found for Nikita Romanov.
Found records for Faduma Khalif:
66334|10KFA2199000|KHALIF|FADUMA|BASHIR||320||MEMORIAL DR||021394910||||||D |10/21/1999|02/12/2020|01|02|8|1311|185|I

Found records for Kahmile Whitby:
67187|11WKE0800000|WHITBY|KAHMILE|ARNOLD||305||MEMORIAL DR||02139|305 MEMORIAL DR|3034|CAMBRIDGE|MA|021394303|U |11/08/2000|10/05/2021|01|02|8|1311|185|A

No records found for Liliana Vela.
No records found for Kaili Liu.
No records found for Natalie Stewart.
Found records for Kendall Yu:
66984|07YKL2000001|YU|KENDALL|||3||AMES ST||02142||||||U |07/20/2000|08/13/2018|01|02|8|1311|185|I

No records found for Ilaisaane Summers.
No records found for Ajinkya Nene.
No records found for Joey Heerens.
Found records for Anna Bair:
67696|09BAA2301005|BAIR|ANNA|SOPHIA||428||MEMORIAL DR||021394310|428 MEMORIAL DR||CAMBRIDGE|MA|021394305|U |09/23/2001|12/13/2022|01|02A|8|1311|201|A

No records found for Alexa Guan.
No records found for Jadorian Paul.
No records found for Rian Flynn.
No records found for Mike Shao.
No records found for Savannah Lawrence.
Found records for Lesley Phillips:
3031|07PLY1845000|PHILLIPS|LESLEY|REBECCA||1643||CAMBRIDGE ST|52|021384357||||||D |07/18/1945|10/05/1982|06|03|6|1311|142|A

No records found for Katherine Guo.
No records found for Margaret Zheng.
Found records for Anushka Ray:
66335|10RAA2199002|RAY|ANUSHKA|||471||MEMORIAL DR||021394319|215 BROOK VILLAGE RD|2|NASHUA|NH|03062|U |10/21/1999|10/17/2018|05|02|8|1311|201|A

No records found for Gohar Khan.
No records found for Lorenzo Shaikewitz.
No records found for Juliana Chew.
Found records for Juan Ferrua:
64731|05FJN2998000|FERRUA|JUAN|ANGELO||372||MEMORIAL DR||021394319||||||U |05/29/1998|10/11/2016|01|02|8|1311|185|I

No records found for Rochel Green.
No records found for Fausto Uribe.
No records found for Aristofanis Rontogiannis.
Found records for Elizabeth Han:
46519|11HEH0797000|HAN|ELIZABETH|JING||290||MASSACHUSETTS AVE||021394958|290 MASSACHUSETTS AVE|331|CAMBRIDGE|MA|021394130|U |11/07/1997|03/06/2020|03|03|8|1311|143|I

No records found for Karina Zhang.
No records found for Angel Yang.
Found records for Maia Campbell:
66484|12CMA0999001|CAMPBELL|MAIA|INGRAM||3||AMES ST||02142||||||D |12/09/1999|02/10/2020|01|02|8|1311|185|I

No records found for Jakob Jarczynski.
No records found for Andy Xu.
No records found for Allen Huang.
Found records for Yossef Baidi:
62945|02BYF0697000|BAIDI|YOSSEF|||105||CHESTNUT ST||02139||||||D |02/06/1997|01/22/2020|05|03|8|1311|143|A

No records found for Ria Das.
Found records for Andrew Chen:
66667|02CAW2500000|CHEN|ANDREW|YEN-JONG||12||WENDELL ST|7|021381848|12 WENDELL ST|7|CAMBRIDGE|MA|021381848|U |02/25/2000|08/01/2022|07|01|6|34|142|A

No records found for Yiwei Zhu.
No records found for Shiyu Chen.
Found records for Lara Shonkwiler:
66012|06SLA2299000|SHONKWILER|LARA|E||89||SCIARAPPA ST|1|02141||||||D |06/22/1999|10/17/2017|02|02|8|1311|143|A

No records found for Pelkins Ajanoh.
No records found for Kaylee Soto.
No records found for Rokas Veitas.
No records found for Megan Montgomery.
Found records for Aditya Mehrotra:
49467|12MAA2699001|MEHROTRA|ADITYA|||88||HAMPSHIRE ST|2|021391767||||||U |12/26/1999|09/13/2022|03|01|8|1311|143|A

Found records for Athena Nguyen:
66037|07NAA0299000|NGUYEN|ATHENA|N||305||MEMORIAL DR||02139||||||D |07/02/1999|10/11/2017|01|02|8|1311|185|A

No records found for Carrie Laber-Smith.
Found records for Oomi Pammit:
67734|10POI2701000|PAMMIT|OOMI|N||229||VASSAR ST||021394310||||||D |10/27/2001|10/16/2019|05|02|8|1311|201|A

No records found for Gabriella Garcia.
No records found for Haimoshri Dali.
Found records for Brandon Epstein:
65258|10EBN2498001|EPSTEIN|BRANDON|R||305||MEMORIAL DR||02139||||||D |10/24/1998|10/11/2017|01|02|8|1311|185|A

No records found for Camila Miranda-Llovera.
Found records for Joshua Lee:
43631|03LJA2696003|LEE|JOSHUA|||20||CHILD ST|903|021411777||||||D |03/26/1996|12/31/2019|01|01|8|1311|185|A

No records found for Tema Nwana.
No records found for Shinjini Ghosh.
No records found for Jess Ding.
No records found for Hengameh Bagherian.
No records found for Shelly Ben-David.
No records found for Stacie Lin.
No records found for Richard Moyer.
Found records for Audrey Shine:
67269|12SAY2400000|SHINE|AUDREY|C||0||CANADAY HL||02138|2357 HARVARD YARD MAIL CENTER||CAMBRIDGE|MA|02138|D |12/24/2000|09/09/2019|07|03|6|1311|142|I

No records found for Valeriia Nin.
No records found for Anna Arpaci-Dusseau.
No records found for Zulkayda Mamat.
No records found for Ijan Zha.
No records found for Giramnah Peña-Alcántara.
No records found for Qiyun Gao.
No records found for John Adeyeye.
Found records for Emily Wang:
51888|07WEY2804000|WANG|EMILY|||290||MASSACHUSETTS AVE||021394958|290 MASSACHUSETTS AVE|442|CAMBRIDGE|MA|02139|D |07/28/2004|10/29/2022|03|03|8|1311|143|A

66761|04WEY1600000|WANG|EMILY|J||450||MEMORIAL DR||021394306||||||D |04/16/2000|10/13/2021|05|02|8|1311|201|A

67844|01WEY2902000|WANG|EMILY|MINSI||362||MEMORIAL DR||021394071|362 MEMORIAL DR||CAMBRIDGE|MA|021394304|D |01/29/2002|11/07/2019|01|02|8|1311|185|A

No records found for Kara Zhang.
No records found for Doris Fu.
No records found for Enrico Colón.
No records found for Nadia Salahuddin.
No records found for Arnav Patel.
No records found for Shan Lu.
No records found for Daniel Hong.
No records found for Lydia Yu.
No records found for Tommie Reerink.
No records found for Rebecca Gallivan.
No records found for Nabil Khalil.
Found records for Laura Conrad:
5535|02CLA2551000|CONRAD|LAURA|E||233||BROADWAY||02139||||||D |02/25/1951|07/19/1996|03|01|8|1311|143|A

No records found for Crista Falk.
No records found for Shushu Fang.
No records found for Sergio Perez.
No records found for Mendel Keller.
No records found for Chris Chang.
No records found for Rishabh Chandra.
No records found for Clare Liu.
No records found for Dean Fanggohans.
No records found for Otilia Don.
No records found for Miles George.
Found records for Mary Dahl:
63960|11DMY0597001|DAHL|MARY|||322||WESTERN AVE||02139||||||D |11/05/1997|02/15/2022|04|03|8|1311|142|A

No records found for Sam Ying.
No records found for Abram Turner.
No records found for Nina Masuelli.
No records found for Elliott Seaman.
No records found for Amanda Deng.
No records found for Eliza Khokhar.
No records found for Dylan Liu.
Found records for Ryan Mansilla:
65781|03MRN2799002|MANSILLA|RYAN|HERBERT||50||CAMBRIDGE PARK DR|242|021402791||||||U |03/27/1999|02/02/2023|11|01A|8|34|146|A

No records found for Robert Henning.
Found records for Joy Ma:
67326|02MJY0201000|MA|JOY|Y||362||MEMORIAL DR||021394071||||||U |02/02/2001|10/16/2019|01|02|8|1311|185|A

No records found for Jeevesh Konuru.
No records found for Rami Manna.
No records found for Arber Bakalli.
No records found for Cameron Hilman.
Found records for Ian McJohn:
66998|01MIN0110002|MCJOHN|IAN|C||202||LEXINGTON AVE||021382138|70 PINE ST|2312|NEW YORK|NY|100050034|U |07/26/2000|07/26/2018|09|02|6|1332|146|A

No records found for Alex Evenchik.
Found records for Michael Weymouth:
63199|04WML1597000|WEYMOUTH|MICHAEL|STEVEN||6||CANAL PARK|206|021412212|6 CANAL PARK|206|CAMBRIDGE|MA|021412212|U |04/15/1997|11/29/2021|02|03|8|1311|185|A

No records found for Sabrina Romero.
No records found for Xiaoxi Wang.
No records found for Michelle Sanchez.
No records found for Trancy Zhu.
No records found for Maryann Chidume.
No records found for Samir Droubi.
No records found for Julianna Rodriguez.
No records found for Max Reese.
Found records for Laura Koemmpel:
63274|05KLA0497000|KOEMMPEL|LAURA|JEAN||89||PLYMOUTH ST|1|02141||||||U |05/04/1997|08/15/2018|02|01|8|1311|143|A

No records found for Willers Yang.
No records found for Stephanie Hu.
No records found for Catherine Yao.
No records found for Noah Raby.
No records found for Carolina Perez.
Found records for Kathleen Kelly:
6408|11KKN2452001|KELLY|KATHLEEN|||47||LAWN ST||021384442||||||D |11/24/1952|07/17/2008|09|03|6|1332|146|A

18651|03KKN0860003|KELLY|KATHLEEN|MAURA||17||MARIE AVE|1|021391002||||||D |03/08/1960|10/01/1991|06|01A|6|1311|143|A

59745|03KKN0395001|KELLY|KATHLEEN|||1||PINE ST||021393513|1 PINE ST||CAMBRIDGE|MA|02139|D |03/03/1995|11/01/2021|03|03|8|1311|143|A

Found records for Uillia O'Connell:
64493|03OLM2698000|O'CONNELL|UILLIA|||17||MARIE AVE|1|021391002|17 MARIE AVE|1|CAMBRIDGE|MA|021391002|D |03/26/1998|04/13/2016|06|01A|6|1311|143|A

No records found for Mark Jabbour.
Found records for Sean Fraser:
61956|06FSN2496001|FRASER|SEAN|CAMERON BURROWS||56||8TH ST||021411542||||||D |06/24/1996|09/28/2019|02|02|8|1311|143|I

No records found for Aj Cox.
Found records for Ellen Shachter:
10842|07SEN0361000|SHACHTER|ELLEN|JUDITH||346||CONCORD AVE|2|021381210|346 CONCORD AVE|2|CAMBRIDGE|MA|021381210|D |07/03/1961|09/20/1986|09|02|6|1332|146|A

No records found for Harry Thaman.
No records found for Suleman Saad.
No records found for Marta Manzin.
No records found for Andres Tarrido-Picart.
Found records for Erik Porter:
65498|01PEK1399000|PORTER|ERIK|JOE||3||AMES ST||02142|3 AMES ST, EAST CAMPUS|B312|CAMBRIDGE|MA|02142|D |01/13/1999|10/10/2018|01|02|8|1311|185|I

No records found for Arsen Vasilyan.
No records found for Gloria Chyr.
No records found for Tien Phung.
No records found for Emily Yuan.
No records found for Willy Wu.
No records found for Michelle Shen.
Found records for Laura Cui:
67627|08CLA0301001|CUI|LAURA|LI||15||PEARL ST|9|021394079|15 PEARL ST|9|CAMBRIDGE|MA|021394079|U |08/03/2001|08/26/2022|05|01|8|1311|143|A

No records found for Xinyi Chen.
Found records for Nadeem Mazen:
41581|09MNM2083000|MAZEN|NADEEM|ABDELMAGID||171||AUBURN ST|2|021393949|45 PROSPECT ST||CAMBRIDGE|MA|021392402|D |09/20/1983|10/28/2011|05|01|8|1311|143|I

No records found for Tyler Higgs.
No records found for Em Oh.
No records found for Zhi Gan.
No records found for Jerry Mei.
No records found for Savva Morozov.
No records found for Lucy Liao.
No records found for Ray Liao.
Found records for Sophia Li:
44710|10LSA0696000|LI|SOPHIA|RUOLAN||331||HARVARD ST|14|021392030||||||D |10/06/1996|02/10/2020|06|03|6|1311|142|I

Found records for Amelie Kharey:
62389|09KAE2796002|KHAREY|AMELIE|NINA||20||HARDING ST|1|021411055|20 HARDING ST|1|CAMBRIDGE|MA|021411055|U |09/27/1996|09/07/2016|01|03|8|1311|143|A

No records found for Mimi Wahid.
No records found for George Chen.
No records found for Megan Diehl.
No records found for Will MacArthur.
No records found for Joyce Noh.
No records found for Eesam Hourani.
Found records for Andison Tran:
65700|02TAN2899000|TRAN|ANDISON|||5||COLUMBIA ST|207|02139||||||U |02/28/1999|10/25/2022|05|01|8|1311|143|A

No records found for Sarah Weidman.
No records found for Talha Faiz.
No records found for Eileen Tan-Aristy.
Found records for Sharon Lin:
65316|11LSN1498001|LIN|SHARON|TING||3||AMES ST||02142||||||D |11/14/1998|10/12/2017|01|02|8|1311|185|I

No records found for Abdullah Bannan.
No records found for Monica Mladenik.
No records found for Jiageng Liu.
Found records for Divya Goel:
63624|07GDA2197001|GOEL|DIVYA|||410||MEMORIAL DR||02139|410 MEMORIAL DR|432C|CAMBRIDGE|MA|02139|U |07/21/1997|02/10/2016|01|02A|8|1311|201|I

Found records for Elina Sendonaris:
65220|10SEA1098005|SENDONARIS|ELINA|MARIA||107||COLUMBIA ST|2|021392777||||||D |10/10/1998|10/01/2020|03|03|8|1311|143|I

No records found for Ben Rowley.
No records found for Lydia Light.
No records found for Luis Trueba.
No records found for Anastasiia Uvarova.
No records found for Ayush Sharma.
Found records for Claire Hsu:
48195|12HCE1698000|HSU|CLAIRE|C||250||KENDALL ST|404|02142||||||D |12/16/1998|10/11/2017|02|03|8|1311|185|I

No records found for Ahaan Rungta.
Found records for Drew Polstra:
45802|05PDW2597000|POLSTRA|DREW|DANIEL||120||RINDGE AVE|106|02140||||||D |05/25/1997|07/17/2020|11|02|8|34|146|A

No records found for Deepankar Gupta.
No records found for Susan Su.
No records found for Jessica Dong.
No records found for Lex Groark.
No records found for Hem Chaudhary.
No records found for Ali Marsh.
Found records for Cristian Rios:
66980|07RCN1900000|RIOS|CRISTIAN|||3||AMES ST||02142|3 AMES ST|G106|CAMBRIDGE|MA|02142|D |07/19/2000|07/05/2019|01|02|8|1311|185|I

No records found for Logan Engstrom.
No records found for Tugsbayasgalan Manlaibaatar.
No records found for Keaten Clarno.
Found records for Brian Williams:
18208|05WBN1259000|WILLIAMS|BRIAN|C||30||MOUNT PLEASANT ST||021402614|30 MOUNT PLEASANT ST||CAMBRIDGE|MA|021402614|D |05/12/1959|04/23/1999|10|02|6|34|142|A

No records found for Juan Ortiz.
No records found for Sawyer Hart.
Found records for Karan Kashyap:
59756|03KKN0795003|KASHYAP|KARAN|||100||MEMORIAL DR||021421318||||||U |03/07/1995|03/02/2020|01|02|8|1311|185|I

No records found for Amber Bick.
Found records for Mydia Phan:
66713|03PMA2500000|PHAN|MYDIA|D||450||MEMORIAL DR||021394306|450 MEMORIAL DR|F327|CAMBRIDGE|MA|02139|D |03/25/2000|10/17/2018|05|02|8|1311|201|A

No records found for Loewen Cavill.
No records found for Benjamin Oberlton.
No records found for Brice Huang.
No records found for Weitung Chen.
Found records for Tony Zhang:
63865|10ZTY0597000|ZHANG|TONY|||500||MEMORIAL DR||02139||||||D |10/05/1997|10/13/2015|05|02|8|1311|201|I

No records found for Erica Waller.
No records found for Kate Nelson.
No records found for Belinda Shi.
No records found for Michelle Bai.
Found records for Alexandra Berg:
53541|01BAA0391006|BERG|ALEXANDRA|||20||ORCHARD ST|3|02140||||||D |01/03/1991|07/05/2019|10|01A|6|34|142|A

No records found for Adit Abraham.
No records found for Tammam Mustafa.
No records found for Mark Mockett.
No records found for Jonathan Kosgei.
No records found for Oyuntugs Luubaatar.
No records found for Anastasiia Alokhina.
No records found for Cindy Gu.
No records found for Margaret Bertoni.
Found records for Rujul Gandhi:
66929|06GRL2400000|GANDHI|RUJUL|R||229||VASSAR ST||021394310|229 VASSAR ST|921C|CAMBRIDGE|MA|02139|U |06/24/2000|10/17/2018|05|02|8|1311|201|A

No records found for Eswar Anandapadmanaban.
No records found for Gabriella Liu.
Found records for Grayson King:
63977|11KGN0997000|KING|GRAYSON|C||3||AMES ST||02142||||||D |11/09/1997|10/12/2017|01|02|8|1311|185|I

Found records for Robert Cato:
67490|05CRT2101000|CATO|ROBERT|LEE|III|450||MEMORIAL DR||021394306|450 MEMORIAL DR|J411|CAMBRIDGE|MA|02139|D |05/21/2001|10/29/2022|05|02|8|1311|201|A

No records found for Kye Burchard.
No records found for Ashley Lee.
No records found for Johan Cervantes.
No records found for Colt DeWolf.
No records found for Aliai Acuil.
No records found for Malte Ahrens.
No records found for Tafsia Shikdar.
No records found for Eren Guttentag.
No records found for Meera Gregerson.
No records found for Trang Luu.
Found records for Marcelo Garcia:
47909|12GMO3187001|GARCIA|MARCELO|||37||5TH ST||021411167|71 12TH AVE||HAVERHILL|MA|018303146|U |12/31/1987|03/31/2021|01|03|8|1311|143|I

No records found for Austin Garrett.
No records found for David Onyemelukwe.
No records found for Alejandra Rojas.
No records found for William Lopez-Cordero.
No records found for Hailey Brace.
No records found for Steven Serrano.
No records found for Celia Han.
No records found for May Huang.
No records found for Dou Dou.
No records found for Sophia Cheung.
No records found for Miguel Gomez.
Found records for Stephanie Fu:
67104|09FSE2100000|FU|STEPHANIE|||320||MEMORIAL DR||021394910||||||D |09/21/2000|10/16/2019|01|02|8|1311|185|A

No records found for Eleane Lema.
No records found for Rebecca Eisenach.
No records found for Ashhad Alam.
No records found for Justin Yu.
Found records for Aryt Alasti:
15613|01AAT2057000|ALASTI|ARYT|||411||FRANKLIN ST|712|021393156|411 FRANKLIN ST|712|CAMBRIDGE|MA|021393156|D |01/20/1957|09/27/2008|04|02|6|1311|142|A

No records found for Nicholas Egan.
No records found for Billy Moses.
No records found for Kristian Georgiev.
Found records for Bruke Kifle:
63686|08KBE0797000|KIFLE|BRUKE|M||305||MEMORIAL DR||02139||||||D |08/07/1997|10/09/2016|01|02|8|1311|185|A

Found records for Jonathan Paras:
61362|02PJN2296001|PARAS|JONATHAN|||55||HAMPSHIRE ST|1|021391692||||||U |02/22/1996|08/31/2020|03|01|8|1311|143|A

No records found for Ben Sorkin.
No records found for José Mendoza.
Found records for Gina Han:
63042|03HGA0497000|HAN|GINA|||413||WASHINGTON ST|3|021392780||||||D |03/04/1997|02/05/2020|03|03|8|1311|143|A

No records found for Njeri Gachoka.
Found records for Wonjune Kang:
63670|08KWE0397001|KANG|WONJUNE|||18||SUFFOLK ST||021392713|18 SUFFOLK ST||CAMBRIDGE|MA|021392713|U |08/03/1997|08/31/2020|03|03|8|1311|143|A

Found records for Rosanna Zhang:
47550|02ZRA0898000|ZHANG|ROSANNA|M||100||MEMORIAL DR|5-10A|021421360|100 MEMORIAL DR|510A|CAMBRIDGE|MA|021421360|U |02/08/1998|10/13/2016|01|02|8|1311|185|I

No records found for Jeanne Harabedian.
Found records for Lani Lee:
66170|08LLI1999000|LEE|LANI|DAKYOUNG||31||INMAN ST||021392406|31 INMAN ST||CAMBRIDGE|MA|021392406|D |08/19/1999|10/18/2017|03|03A|6|1311|142|A

No records found for Rahul Ramakrishnan.
No records found for Tim Chong.
No records found for Long Nguyen.
Found records for Kevin Pho:
66557|01PKN0700003|PHO|KEVIN|KHOA||471||MEMORIAL DR||021394319||||||U |01/07/2000|10/17/2018|05|02|8|1311|201|I

No records found for Josh Cole.
No records found for Sharlene Song.
Found records for Jonathan Anjaria:
36419|04AJN2679002|ANJARIA|JONATHAN|S||10||WORCESTER ST|2|021392715|10 WORCESTER ST|2|CAMBRIDGE|MA|021392715|D |04/26/1979|07/12/2007|03|03|8|1311|143|A

Found records for Eric Lin:
43158|12LEC1284000|LIN|ERIC|||57||MAGAZINE ST|2|021393966|57 MAGAZINE ST|2|CAMBRIDGE|MA|021393966|U |12/12/1984|12/27/2019|04|03|8|1311|142|A

Found records for David Mueller:
48259|03MDD0388002|MUELLER|DAVID|RAYMOND||152||GORE ST|3|021411135|24 MAGAZINE ST|2|CAMBRIDGE|MA|021393946|U |03/03/1988|06/11/2021|01|03|8|1311|143|A

No records found for George Sun.
No records found for Sara Ki.
Found records for Michael Amoako:
45848|06AML0197000|AMOAKO|MICHAEL|||20||CHILD ST|1506|021411787||||||D |06/01/1997|10/11/2016|01|01|8|1311|185|I

No records found for Henri Champigneulle.
Found records for Kevin Zheng:
64898|06ZKN2998000|ZHENG|KEVIN|ZHOU||945||MEMORIAL DR||021386123|945 MEMORIAL DR||CAMBRIDGE|MA|021386123|U |06/29/1998|02/13/2023|06|02|6|1311|142|A

No records found for Caitlin Shkuratov.
No records found for Victoria DiTomasso.
No records found for Brent Avery.
No records found for Nick Martin.
No records found for Charlie Garcia.
Found records for Andrew Bartow:
42967|11BAW1295001|BARTOW|ANDREW|JOSEPH||350||3RD ST|2015|021421145||||||D |11/12/1995|10/17/2018|02|03|8|1311|185|A

No records found for Jose Gomez.
No records found for Christina Jung.
No records found for Daniel León.
No records found for Ann Quan.
No records found for Nick Charchut.
Found records for David Mejorado:
64487|03MDD2498000|MEJORADO|DAVID||III|2||CHESTNUT ST|34|021394847||||||D |03/24/1998|10/18/2016|05|03|8|1311|143|A

Found records for Kavish Gandhi:
45579|04GKH0997003|GANDHI|KAVISH|||376||WINDSOR ST|1|02141||||||D |04/09/1997|02/09/2016|02|01|8|1311|143|A

No records found for Ilana Nazari.
No records found for Tee Udomlumleart.
Found records for Agatha Tam:
65617|12TAA2098002|TAM|AGATHA|||216||COLUMBIA ST|2|02139||||||D |12/20/1998|11/01/2021|03|01|8|1311|143|A

No records found for Maya Nasr.
No records found for Bryan Chen.
No records found for Maddie Sutula.
No records found for Margaret Manto.
No records found for Evi Postelnicu.
No records found for Jack Reid.
No records found for Tesla Wells.
No records found for Fernando Rendón.
No records found for Jason Seibel.
No records found for Cat Zeng.
No records found for Mario Martinez.
No records found for Liz Martin.
No records found for Nadia Dimitrova.
No records found for Emille Santos.
Found records for John Peurifoy:
61544|03PJN2896002|PEURIFOY|JOHN|EDWARD||351||MASSACHUSETTS AVE||02139|351 MASSACHUSETTS AVE ALPHA DELTA P||CAMBRIDGE|MA|02139|R |03/28/1996|10/14/2016|03|03|8|1311|143|I

No records found for Nate Rodman.
No records found for Sylvie Lee.
No records found for Shraman Chaudhuri.
No records found for Jennifer Walsh.
No records found for Korrawat Pruegsanusak.
Found records for Kayla Vodehnal:
47585|07VKA0898002|VODEHNAL|KAYLA|NICOLE||55||HAMPSHIRE ST|3|02139|55 HAMPSHIRE ST|3|CAMBRIDGE|MA|021391692|D |07/08/1998|08/31/2020|03|01|8|1311|143|I

Found records for Jivan Sobrinho-Wheeler:
55152|03SJN2692004|SOBRINHO-WHEELER|JIVAN|G||187||BROOKLINE ST|3|021394678|187 BROOKLINE ST|3|CAMBRIDGE|MA|021394678|D |03/26/1992|03/28/2018|05|01|8|1311|143|A

No records found for Sam Judd.
No records found for Kelsey Becker.
Found records for Jake Burga:
42594|09BJE1195001|BURGA|JAKE|RYAN||113|1/2|THORNDIKE ST||021411743||||||D |09/11/1995|10/05/2018|02|02|8|1311|143|A

No records found for Liew Min.
No records found for Radhika Bhatt.
No records found for Abhiti Vaish.
No records found for Jenna Hong.
No records found for Alice Zhu.
No records found for Sienna Ramos.
No records found for Xavier Luhman.
No records found for Gabriel Li.
No records found for Jimmy Koppel.
No records found for Talia Khan.
Found records for Marek Subernat:
63524|06SMK1897000|SUBERNAT|MAREK|DAMIAN||233||MASSACHUSETTS AVE||02139||||||U |06/18/1997|02/06/2016|03|03|8|1311|143|I

Found records for Jennifer Leung:
64127|12LJR1097001|LEUNG|JENNIFER|||494||CAMBRIDGE ST|B|021411113|494 CAMBRIDGE ST|B|CAMBRIDGE|MA|021411113|U |12/10/1997|04/26/2023|02|02|8|1311|143|A

No records found for Phoebe Cai.
No records found for Chien-Min Lu.
No records found for David Magrefty.
No records found for Amir Farhat.
No records found for Anthony Occidentale.
No records found for Wilson Gomarga.
No records found for Neil Aggarwal.
No records found for Lucy Sternbach.
No records found for Richard Zhang.
Found records for Elijah Booker:
43053|12BEH1995001|BOOKER|ELIJAH|KIAMBU||130||CAMBRIDGE PARK DR|356|021402565||||||U |12/19/1995|01/09/2014|11|01|8|34|141|A

No records found for Vlad Șeremet.
No records found for Colin Godwin.
No records found for Charlie Marquardt.
No records found for Ty Bellitti.
No records found for Sarah Melvin.
No records found for Kyl Nero.
Found records for Alex Chen:
62686|12CAX1296000|CHEN|ALEX|LIU||19||PLEASANT ST|1|021393735|19 PLEASANT ST|1|CAMBRIDGE|MA|021393735|U |12/12/1996|06/30/2022|04|02|6|1311|142|A

No records found for Jonathan Buschel.
Found records for Sophie Fisher:
64080|12FSE0897001|FISHER|SOPHIE|ELIZA||83||CAMBRIDGE PKWY|W901|021421244||||||D |12/08/1997|12/09/2021|01|02|8|1311|185|A

No records found for Jae Kim.
No records found for René Franceschini.
Found records for Nathan Hunt:
56140|11HNN1692000|HUNT|NATHAN|RAY||11||AUDREY ST||021394907|11 AUDREY ST|A4|CAMBRIDGE|MA|021394950|U |11/16/1992|10/19/2016|05|02|8|1311|201|A

No records found for Sophia Chan.
Found records for Moin Nadeem:
47506|06NMN0498000|NADEEM|MOIN|||129||FRANKLIN ST|113|02139||||||U |06/04/1998|09/19/2016|05|01|8|1311|143|I

Found records for Daniel Mascoop:
39293|11MDL0293001|MASCOOP|DANIEL|ROSS||37||SPERIDAKIS TER||021394017||||||U |11/02/1993|08/07/2018|05|01|8|1311|143|A

No records found for Aaron Huang.
Found records for Paul Toner:
24176|04TPL2866000|TONER|PAUL|F||24||NEWMAN ST||021401013||||||D |04/28/1966|08/18/1984|11|03|6|34|141|A

Found records for Sarah Block:
23330|05BSH0565001|BLOCK|SARAH|E||24||SHEPARD ST|2|021381522||||||D |05/05/1965|02/09/2000|08|01|6|34|142|A

Found records for Samuel Liu:
61213|01LSL1796002|LIU|SAMUEL|||240||ALLSTON ST|3|02139||||||U |01/17/1996|10/04/2021|04|01|8|1311|143|I

Found records for Davis Tran:
41066|12TDS2094001|TRAN|DAVIS|||25||FAIRFIELD ST|3|021401922||||||D |12/20/1994|10/15/2019|10|01|8|34|146|I

No records found for Prianca Tawde.
No records found for Ray Tsou.
No records found for Kathy Watkins.
Found records for Dana Bullister:
32541|06BDA0890001|BULLISTER|DANA|RAY||155||5TH ST|1|021412031|155 5TH ST|1|CAMBRIDGE|MA|021412031|D |06/08/1990|06/04/2016|02|02|8|1311|143|A

No records found for TC Jiang.
Found records for Robert Barnes:
55437|05BRT2892001|BARNES|ROBERT|||13||HOWLAND ST||02138||||||D |05/28/1992|10/02/2017|07|01|6|34|142|I

No records found for Jess Nahigian.
No records found for Cody Burton.
Found records for Julia Lee:
60233|06LJA1395000|LEE|JULIA|||1925||MASSACHUSETTS AVE|3|021401401|1925 MASSACHUSETTS AVE|3|CAMBRIDGE|MA|021401401|U |06/13/1995|11/18/2022|10|02|6|34|142|A

No records found for Sumit Aggarwal.
No records found for Angie Boggust.
Found records for Mark Boswell:
15523|02BMK1370000|BOSWELL|MARK|ALAN||105||WALDEN ST||021403304|105 WALDEN ST||CAMBRIDGE|MA|021403304|D |02/13/1970|01/07/2008|10|02|6|34|142|A

Found records for Connie Xu:
63576|07XCE0597000|XU|CONNIE|||47||BISHP ALLEN DR|301|02139||||||D |07/05/1997|10/13/2021|03|03|8|1311|143|A

Found records for Ian Tracy:
32304|04TIN2190001|TRACY|IAN|PATRICK||14||CONCORD AVE||021382356|70 PACIFIC ST||CAMBRIDGE|MA|021394204|U |04/21/1990|05/25/2016|08|02|6|1332|142|I

Found records for Michael Scarlett:
61551|03SML3096004|SCARLETT|MICHAEL|D||22||ALPINE ST||021386811||||||D |03/30/1996|06/05/2014|09|02|6|1332|146|A

Found records for Haihao Liu:
62434|10LHO0696000|LIU|HAIHAO|||54||PORTSMOUTH ST|3|02141|54 PORTSMOUTH ST|3|CAMBRIDGE|MA|021411328|D |10/06/1996|09/25/2020|02|01|8|1311|143|A

No records found for Aneeqa Muzammil.
No records found for Mads Bragg.
No records found for Elyse Paneral.
No records found for Alexandra Markiewicz.
No records found for Logan Abel.
No records found for Udayan Umapathi.
Found records for Theodore Caputi:
58980|08CTE2594001|CAPUTI|THEODORE|LEWIS||100||MEMORIAL DR||021421318|100 MEMORIAL DR||CAMBRIDGE|MA|021421314|D |08/25/1994|08/16/2018|01|02|8|1311|185|A

No records found for Anna Waldman-Brown.
Found records for Banti Gheneti:
59638|02GBI0595001|GHENETI|BANTI|||17||PLEASANT PL||021393801||||||U |02/05/1995|09/16/2019|04|03|8|1311|142|A

Found records for Ari Epstein:
20713|06EAI2162002|EPSTEIN|ARI|W||146||RAYMOND ST||021403315|146 RAYMOND ST||CAMBRIDGE|MA|02140|D |06/21/1962|01/25/1999|10|03|8|34|146|A

No records found for Shreyas Kapur.
No records found for Joe Scherrer.
Found records for Paul Anders:
1816|10APL2337000|ANDERS|PAUL|EMILE||154||AUBURN ST|1E|02139||||||D |10/23/1937|09/12/1984|05|01|8|1311|143|A

No records found for Nick Morgante.
No records found for Mahi Shafiullah.
No records found for Hongyi Shi.
No records found for Dominic Russel.
No records found for Heather McArdle.
No records found for Novalia Tjandrasaputra.
No records found for Georgia Gutierrez.
No records found for Tammy Che.
No records found for Allie Daley.
No records found for Mohammed Medhat.
Found records for Vatsady Sivongxay:
23600|02SVY2082001|SIVONGXAY|VATSADY|NICLA||5||WORCESTER ST||02139||||||D |02/20/1982|09/01/2016|03|03|8|1311|143|A

No records found for David Morczinek.
No records found for Gisela González.
No records found for Becca Reid.
Found records for Carolyn Fuller:
4133|01FCN1148000|FULLER|CAROLYN|A||12||DOUGLASS ST||021393404||||||D |01/11/1948|06/03/1981|05|01|8|1311|143|A

No records found for Khatantuul Zorig.
No records found for Antonella Masini.
No records found for Riana Shaah.
Found records for Ann Tennis:
2536|09TAN2143000|TENNIS|ANN|MANNING||71||GRISWOLD ST|2|021381035|71 GRISWOLD ST||CAMBRIDGE|MA|021381035|U |09/21/1943|04/16/1980|09|02|6|1332|146|A

Found records for Quinton Zondervan:
28267|09ZQN1570001|ZONDERVAN|QUINTON|Y||235||CARD MEDEIROS AVE||021411921|519 SOMERVILLE AVE  PMB 214||SOMERVILLE|MA|02143|D |09/15/1970|06/04/2004|02|01|8|1311|143|A

Found records for Fiona Grant:
59459|12GFA1894002|GRANT|FIONA|||1524||CAMBRIDGE ST|6|02139||||||D |12/18/1994|08/10/2018|06|03|6|1311|142|A

No records found for Willie Boag.
Found records for Carolyn Lu:
61440|01LCN0196010|LU|CAROLYN|||12|A|SAGINAW AVE|A|02140|84 CUTTERS RIDGE RD||CARLISLE|MA|017411143|D |03/03/1996|11/23/2020|10|02|6|34|142|A

No records found for Jose Barriga.
No records found for Doug Brown.
Found records for Theodora Skeadas:
32811|08STA1690002|SKEADAS|THEODORA|THEO||988||MEMORIAL DR|185|02138||||||D |08/16/1990|06/10/2016|08|02|6|1332|142|A

Found records for Joshua Gerber:
22041|01GJA0980001|GERBER|JOSHUA|WOLF||4||UNION ST||021391511|4 UNION ST||CAMBRIDGE|MA|021391511|D |01/09/1980|10/10/2015|03|02|8|1311|143|A

No records found for Ju Chulakadabba.
No records found for Janny Shafer.
No records found for Jinane Abounadi.
No records found for Janie Katz-Christy.
Found records for Craig Kelley:
11523|09KCG1862000|KELLEY|CRAIG|A||6||SAINT GERARD TER|2|021401824||||||D |09/18/1962|06/09/1993|10|01|8|34|146|A

No records found for Prem Sharma.
Found records for Joan Epstein:
23981|02EJN2066001|EPSTEIN|JOAN|SILBERLICHT||146||RAYMOND ST||021403315|146 RAYMOND ST||CAMBRIDGE|MA|021403315|D |02/20/1966|10/09/1990|10|03|8|34|146|A

No records found for Saul Wilson.
Found records for Dirk Stahlecker:
39285|01SDK2694003|STAHLECKER|DIRK|GEOFFREY||20||RINDGE AVE|2|021401907||||||D |01/26/1994|08/23/2016|10|01|8|34|146|A

Found records for Samuel Gebru:
54701|01GSL0108000|GEBRU|SAMUEL|||812||MEMORIAL DR|614A|021394627|812 MEMORIAL DR|614A|CAMBRIDGE|MA|021394638|D |11/20/1991|05/14/2010|04|01|8|1311|143|A

Found records for Charles Franklin:
55554|06FCS2792002|FRANKLIN|CHARLES|J||162||HAMPSHIRE ST|1R|021391367|162 HAMPSHIRE ST|1R|CAMBRIDGE|MA|021391367|D |06/27/1992|12/02/2016|03|02|8|1311|143|A

Found records for Lisa Griffith:
29005|08GLA2471001|GRIFFITH|LISA|A||111||MAGAZINE ST|2|02139||||||D |08/24/1971|11/04/2008|04|01|8|1311|143|A

Found records for Susan Fleischmann:
13881|02FSN2455000|FLEISCHMANN|SUSAN|D||5||SAINT MARY RD|2|021391220||||||D |02/24/1955|09/22/1981|06|01|8|1311|143|A

No records found for Manikka Bowman.
Found records for Michael Fournier:
35535|07FML0578001|FOURNIER|MICHAEL|DAVID||8||CRAIGIE CIR|45|02138||||||D |07/05/1978|09/06/2005|08|02|6|1332|142|A

Found records for Santos Carrasquillo:
31467|09CSS2589000|CARRASQUILLO|SANTOS|||188||HARVARD ST|3B|021392749|188 HARVARD ST|3B|CAMBRIDGE|MA|021392749|U |09/25/1989|08/28/2015|03|03|8|1311|143|A

Found records for Sandya Subramanian:
57093|07SSA0293005|SUBRAMANIAN|SANDYA|||70||PACIFIC ST||021394204|70 PACIFIC ST|540C|CAMBRIDGE|MA|02139|D |07/02/1993|10/13/2017|05|03|8|1311|143|I

Found records for Wylie Chang:
60598|09CWE0295000|CHANG|WYLIE|DANIEL CHEN-HSI||14||FARWELL PL||021383729|14 FARWELL PL||CAMBRIDGE|MA|021383729|D |09/02/1995|06/10/2020|08|02|6|1332|142|A

No records found for Sally Beiruti.
Found records for Peter Crawley:
18867|06CPR1360000|CRAWLEY|PETER|A||88||THORNDIKE ST||021411745|88 THORNDIKE ST||CAMBRIDGE|MA|021411745|D |06/13/1960|10/19/2005|02|02|8|1311|143|A

Found records for David Oberschmidt:
17424|12ODD2172000|OBERSCHMIDT|DAVID|||223||CONCORD TPKE|110|021402320|223 CONCORD TPKE|110|CAMBRIDGE|MA|021402320|D |12/21/1972|10/01/2016|11|01|8|34|141|A

Found records for Ayesha Wilson:
39829|04WAA2682003|WILSON|AYESHA|M||15||CONCORD AVE|1|021382321||||||D |04/26/1982|11/14/2017|08|02|6|1332|142|A

No records found for Héctor Jesús-Cortés.
No records found for Erin Saif.
Found records for Emina Becirovic:
33049|09BEA2090000|BECIROVIC|EMINA|||123||CHERRY ST|2|02139||||||D |09/20/1990|02/13/2016|03|03|8|1311|143|A

Found records for Justin Saif:
19880|11SJN0576000|SAIF|JUSTIN|N||259||HURLEY ST|4|02141||||||D |11/05/1976|10/13/2004|02|02|8|1311|143|A

Found records for Bret Matthew:
50866|05MBT2189002|MATTHEW|BRET|A||22||WATER ST|1503|02141||||||D |05/21/1989|08/19/2014|01|03|8|1311|143|A

Found records for John Campbell:
33542|07CJN0976006|CAMPBELL|JOHN|||30||HOLWORTHY PL|2|02138||||||U |07/09/1976|03/12/2007|09|03|6|1332|146|A

45294|06CJN0786001|CAMPBELL|JOHN|ROSS||189||VASSAR ST||02139|189 VASSAR ST|4207|CAMBRIDGE|MA|021394330|D |06/07/1986|06/26/2015|05|02|8|1311|201|A

No records found for Alicia Rodríguez.
Found records for Ryan Davis:
55934|09DRN2892000|DAVIS|RYAN|I||47||HOMER AVE|32|021384542|47 HOMER AVE|32|CAMBRIDGE|MA|021384542|D |09/28/1992|09/05/2018|09|03|6|1332|146|A

No records found for Solomon Steen.
Found records for Mike Connolly:
37659|06CML0380000|CONNOLLY|MIKE|||4||ASHBURTON PL|1|021392610||||||D |06/03/1980|10/17/2011|03|03|8|1311|143|A

No records found for Danny Hidalgo.
Found records for Johnny Yang:
39642|03YJY2082000|YANG|JOHNNY|TSUNGYU||103||GORE ST|1|021411234|103 GORE ST|1|CAMBRIDGE|MA|021411200|U |03/20/1982|09/05/2008|01|03|8|1311|143|A

Found records for Anne Hunter:
10301|03HAE2651000|HUNTER|ANNE|M||10||ROGERS ST|518|021421249||||||U |03/26/1951|06/05/1991|02|03|8|1311|185|A

Found records for Nadeem Mazen:
41581|09MNM2083000|MAZEN|NADEEM|ABDELMAGID||171||AUBURN ST|2|021393949|45 PROSPECT ST||CAMBRIDGE|MA|021392402|D |09/20/1983|10/28/2011|05|01|8|1311|143|I

"""

pattern = r"(Found records for) ([\w\s\-]+):?"
matches = re.findall(pattern, response_text)

names = [match[1] for match in matches]
print(names)
