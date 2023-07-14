<map version="freeplane 1.9.13">
<!--To view this file, download free mind mapping software Freeplane from https://www.freeplane.org -->
<node TEXT="FIA3" LOCALIZED_STYLE_REF="AutomaticLayout.level.root" FOLDED="false" ID="ID_696401721" CREATED="1610381621824" MODIFIED="1689302858280"><hook NAME="MapStyle" zoom="1.001">
    <properties edgeColorConfiguration="#808080ff,#ff0000ff,#0000ffff,#00ff00ff,#ff00ffff,#00ffffff,#7c0000ff,#00007cff,#007c00ff,#7c007cff,#007c7cff,#7c7c00ff" show_icon_for_attributes="true" associatedTemplateLocation="template:/standard-1.6.mm" show_note_icons="true" fit_to_viewport="false"/>

<map_styles>
<stylenode LOCALIZED_TEXT="styles.root_node" STYLE="oval" UNIFORM_SHAPE="true" VGAP_QUANTITY="24 pt">
<font SIZE="24"/>
<stylenode LOCALIZED_TEXT="styles.predefined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="default" ID="ID_271890427" ICON_SIZE="12 pt" COLOR="#000000" STYLE="fork">
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="200" DASH="" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_271890427" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<font NAME="SansSerif" SIZE="10" BOLD="false" ITALIC="false"/>
<richcontent CONTENT-TYPE="plain/auto" TYPE="DETAILS"/>
<richcontent TYPE="NOTE" CONTENT-TYPE="plain/auto"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.details"/>
<stylenode LOCALIZED_TEXT="defaultstyle.attributes">
<font SIZE="9"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.note" COLOR="#000000" BACKGROUND_COLOR="#ffffff" TEXT_ALIGN="LEFT"/>
<stylenode LOCALIZED_TEXT="defaultstyle.floating">
<edge STYLE="hide_edge"/>
<cloud COLOR="#f0f0f0" SHAPE="ROUND_RECT"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.selection" BACKGROUND_COLOR="#afd3f7" BORDER_COLOR_LIKE_EDGE="false" BORDER_COLOR="#afd3f7"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.user-defined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="styles.topic" COLOR="#18898b" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subtopic" COLOR="#cc3300" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subsubtopic" COLOR="#669900">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.important" ID="ID_67550811">
<icon BUILTIN="yes"/>
<arrowlink COLOR="#003399" TRANSPARENCY="255" DESTINATION="ID_67550811"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.AutomaticLayout" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="AutomaticLayout.level.root" COLOR="#000000" STYLE="oval" SHAPE_HORIZONTAL_MARGIN="10 pt" SHAPE_VERTICAL_MARGIN="10 pt">
<font SIZE="18"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,1" COLOR="#0033ff">
<font SIZE="16"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,2" COLOR="#00b439">
<font SIZE="14"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,3" COLOR="#990000">
<font SIZE="12"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,4" COLOR="#111111">
<font SIZE="10"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,5"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,6"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,7"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,8"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,9"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,10"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,11"/>
</stylenode>
</stylenode>
</map_styles>
</hook>
<hook NAME="AutomaticEdgeColor" COUNTER="6" RULE="ON_BRANCH_CREATION"/>
<hook NAME="accessories/plugins/AutomaticLayout.properties" VALUE="HEADINGS"/>
<node TEXT="Synthesis and Evaluation" LOCALIZED_STYLE_REF="AutomaticLayout.level,1" POSITION="right" ID="ID_1272892949" CREATED="1675378365291" MODIFIED="1689304189150" HGAP_QUANTITY="1.25 pt" VSHIFT_QUANTITY="-57 pt">
<edge COLOR="#00ff00"/>
<node TEXT="Data Elements" ID="ID_656775739" CREATED="1675379897492" MODIFIED="1675380802750">
<node TEXT="The four data elements in this project are the patient data element, the test types data element, the appointment data element and the appointment-type data element. The patient data element stores all of the data for the patients, like their age and contact details. The test types data element stores all of the tests that Bundaberg Physiology offers, like the test name, code, price and description. The appointment data element will store the relevant information for an appointment, like if their balance has been paid, who got the appointment, when it was, and what the results of that appointment were. The appointment-type data element stores a link between the appointment and test types, storing the ID of a test for the ID of a test type, to indicate what tests were done in an appointment." ID="ID_1486799305" CREATED="1677644166589" MODIFIED="1689303997352"/>
</node>
<node TEXT="Technical Proposal" ID="ID_1772920001" CREATED="1675380774597" MODIFIED="1675380781257">
<node TEXT="Mind-map (this document)" ID="ID_1949811753" CREATED="1677644175107" MODIFIED="1679977398441"/>
<node TEXT="Prescribed Criteria" ID="ID_1164052283" CREATED="1679977406302" MODIFIED="1679977421539"/>
<node TEXT="Self-determined Criteria" ID="ID_551215880" CREATED="1679977407180" MODIFIED="1679977437842"/>
<node TEXT="Tools and Languages" ID="ID_1593106323" CREATED="1689304036529" MODIFIED="1689304040817"/>
<node TEXT="Dataflow diagram" ID="ID_994120383" CREATED="1679977404198" MODIFIED="1679977413728"/>
<node TEXT="Entity Relationship Diagram" ID="ID_1970058076" CREATED="1689304088073" MODIFIED="1689304097920"/>
<node TEXT="Conceptual Schema" ID="ID_338927591" CREATED="1689304101021" MODIFIED="1689304105619"/>
<node TEXT="Concrete Schema" ID="ID_1976093890" CREATED="1689304107454" MODIFIED="1689304111590"/>
<node TEXT="Analysis of Concrete Schema" ID="ID_629807418" CREATED="1689304112950" MODIFIED="1689304117851"/>
<node TEXT="User interface sketches" ID="ID_1578725565" CREATED="1689304124492" MODIFIED="1689304135421"/>
<node TEXT="Psuedocode" ID="ID_336176430" CREATED="1679977407451" MODIFIED="1679977533846"/>
<node TEXT="Images of Code running" ID="ID_1323652576" CREATED="1679977407346" MODIFIED="1679977450109"/>
<node TEXT="Evaluation" ID="ID_877984992" CREATED="1679977544149" MODIFIED="1679977552348"/>
<node TEXT="Refinements" ID="ID_252915034" CREATED="1689304152683" MODIFIED="1689304155137"/>
<node TEXT="Video" ID="ID_567941325" CREATED="1689304158188" MODIFIED="1689304162142"/>
<node TEXT="References" ID="ID_1279619981" CREATED="1679977554193" MODIFIED="1679977559068"/>
<node TEXT="Annotated Code" ID="ID_267417299" CREATED="1679977561130" MODIFIED="1679977577264"/>
</node>
<node TEXT="Algorithm Components" ID="ID_1392729881" CREATED="1675380804926" MODIFIED="1689304189150" HGAP_QUANTITY="30.5 pt" VSHIFT_QUANTITY="21.75 pt">
<node TEXT="All of the algorithm components this project has relates to three main concepts, listing, searching and inserting. It is able to list the patient names and test codes and appointment summaries. It is able to view and edit appointments and their results, what tests Bundaberg Physio offers, and what patients are in the system." ID="ID_1554046388" CREATED="1677644187440" MODIFIED="1689304299223" HGAP_QUANTITY="5.75 pt" VSHIFT_QUANTITY="-9 pt"/>
</node>
</node>
<node TEXT="Comprehension" POSITION="left" ID="ID_1266789622" CREATED="1675379903453" MODIFIED="1683693185215" HGAP_QUANTITY="-39.25 pt" VSHIFT_QUANTITY="-74.25 pt">
<edge COLOR="#ff00ff"/>
<node TEXT="Data Structures" ID="ID_904142471" CREATED="1675379914364" MODIFIED="1689303003541" HGAP_QUANTITY="26.75 pt" VSHIFT_QUANTITY="-78.75 pt">
<node TEXT="Patient" ID="ID_812476304" CREATED="1689302970065" MODIFIED="1689302974140">
<node TEXT="This data structure holds relevant information about a patient, it stores their name, date of birth, address, postcode, height, weight. This, when combined with a id, allows the program to make calls to the data structure to retrieve the relevant patient information." ID="ID_56267396" CREATED="1689303148414" MODIFIED="1689307055730"/>
</node>
<node TEXT="Appointment" ID="ID_1430805669" CREATED="1689302976964" MODIFIED="1689303005536">
<node TEXT="This data structure holds relevant information about an appointment, it stores the patient&apos;s id, date of appointment, results, and whether it has been paid or not. This, when combined with a id, allows the program to make calls to the data structure to retrieve the relevant appointment information." ID="ID_278614449" CREATED="1689303150725" MODIFIED="1689307130082"/>
</node>
<node TEXT="Types" ID="ID_1671409463" CREATED="1689303011162" MODIFIED="1689303123424">
<node TEXT="This data structure holds relevant information about a test type, it stores the test&apos;s code, name, price, and it&apos;s description. This, when combined with a id, allows the program to make calls to the data structure to retrieve the relevant test information." ID="ID_135899020" CREATED="1689303125388" MODIFIED="1689307341375"/>
</node>
<node TEXT="Appointment-Type" ID="ID_392290928" CREATED="1689303128226" MODIFIED="1689307342860">
<node TEXT="This data structure holds two entities, these entities hold an id for an appointment and an id for a test type, this allows the program to retrieve all appointments that have had a specific test, or all tests that were done during an appointment." ID="ID_440381005" CREATED="1689303153197" MODIFIED="1689307409973"/>
</node>
</node>
<node TEXT="User Experiences" ID="ID_1727187053" CREATED="1675379934736" MODIFIED="1679007809118" HGAP_QUANTITY="23 pt" VSHIFT_QUANTITY="-5.66667 pt">
<node TEXT="The program has a graphical user interface (GUI) to operate the software. It will have a menubar and sidebar system to navigate through the several different pages that will offer different functionality. These will stay on the screen the whole time, using icons and other indicators to allow the users to quickly learn the system." ID="ID_790289489" CREATED="1675392323108" MODIFIED="1689303506242" HGAP_QUANTITY="20.75 pt" VSHIFT_QUANTITY="21.97222 pt"/>
</node>
<node TEXT="Programming Elements" ID="ID_576082470" CREATED="1675380335537" MODIFIED="1683691716137" HGAP_QUANTITY="16.25 pt" VSHIFT_QUANTITY="13.5 pt">
<node TEXT="" ID="ID_788734141" CREATED="1675393870425" MODIFIED="1675393870425">
<hook NAME="FirstGroupNode"/>
</node>
<node TEXT="Saving to SQLite" LOCALIZED_STYLE_REF="AutomaticLayout.level,3" ID="ID_1588012498" CREATED="1675393595195" MODIFIED="1689303516303"/>
<node TEXT="Retrieving from SQLite" LOCALIZED_STYLE_REF="AutomaticLayout.level,3" ID="ID_1044265206" CREATED="1675393602949" MODIFIED="1689303530126"/>
<node TEXT="PyQT UI" LOCALIZED_STYLE_REF="AutomaticLayout.level,3" ID="ID_373185389" CREATED="1675393861489" MODIFIED="1689303552091"/>
<node TEXT="" ID="ID_549825350" CREATED="1675393870425" MODIFIED="1675559891509">
<hook NAME="SummaryNode"/>
<hook NAME="AlwaysUnfoldedNode"/>
<node TEXT="These two major features, those being SQLite and PyQt will allow the user to have a seamless experience throughout the program. The PyQt UI will offer a intuitive system for the user to use to interface with the program. The SQLite database will offer the ability to store the user&apos;s data so that they are able to make sure that their inputted data will be kept safe, and not lost due to the program crashing or other factors which may make the program suddenly stop." ID="ID_1061682953" CREATED="1675393870425" MODIFIED="1689303679038" HGAP_QUANTITY="16.11111 pt" VSHIFT_QUANTITY="-2.11111 pt"/>
</node>
</node>
<node TEXT="Usability Principles" ID="ID_1745692713" CREATED="1683691700091" MODIFIED="1683693185214" HGAP_QUANTITY="13.25 pt" VSHIFT_QUANTITY="34.5 pt">
<node TEXT="" ID="ID_718013615" CREATED="1683691978765" MODIFIED="1683691978765">
<node TEXT="Accessibility" LOCALIZED_STYLE_REF="AutomaticLayout.level,3" ID="ID_796221581" CREATED="1683691979399" MODIFIED="1683693119418">
<node TEXT="The application will have the ability to be used by many different people, even those with disabilities." ID="ID_1110022543" CREATED="1683693121606" MODIFIED="1683693796700"/>
</node>
</node>
<node TEXT="Effectiveness" ID="ID_1361608350" CREATED="1683692980472" MODIFIED="1683692990698">
<node TEXT="The application will have the ability for users to use the system to do the work they need to do, closely related to reliability." ID="ID_1727883534" CREATED="1683693019033" MODIFIED="1683693798657"/>
</node>
<node TEXT="Safety" ID="ID_1547747332" CREATED="1683692981938" MODIFIED="1683693027563">
<node TEXT="The application has the ability for users to make errors and recover from the mistake." ID="ID_1086325519" CREATED="1683693106901" MODIFIED="1683693832295"/>
</node>
<node TEXT="Utility" ID="ID_1095072502" CREATED="1683692982127" MODIFIED="1683693049197">
<node TEXT="The application will need the ability for the system to provide all the functionality that users need" ID="ID_1910034338" CREATED="1683693108064" MODIFIED="1683693872869"/>
</node>
<node TEXT="Learnability" ID="ID_1466513960" CREATED="1683692982708" MODIFIED="1683693086200">
<node TEXT="The application would need to be easy to learn quickly for users." ID="ID_1263176903" CREATED="1683693108896" MODIFIED="1683694258801"/>
</node>
</node>
</node>
<node TEXT="Analysis" POSITION="right" ID="ID_1893631324" CREATED="1675380345373" MODIFIED="1679977688519" HGAP_QUANTITY="21.5 pt" VSHIFT_QUANTITY="49.5 pt">
<edge COLOR="#00ffff"/>
<node TEXT="Programming Requirements" ID="ID_173884441" CREATED="1675381171125" MODIFIED="1675381175742">
<node TEXT="The requirements for the program to be successful would be that firstly, programming elements described are implemented properly, secondly, being that the program is able to successfully save, retrieve, and edit the data structures described." ID="ID_572044311" CREATED="1675399072922" MODIFIED="1689304323096">
<arrowlink DESTINATION="ID_576082470" STARTINCLINATION="-205.49999 pt;-48 pt;" ENDINCLINATION="-78.75 pt;3.75 pt;"/>
<arrowlink DESTINATION="ID_904142471" STARTINCLINATION="-134.25 pt;-41.25 pt;" ENDINCLINATION="-15.75 pt;35.25 pt;"/>
</node>
</node>
<node TEXT="Problem and Solutions" ID="ID_1380890512" CREATED="1675381190896" MODIFIED="1677541217170">
<node TEXT="The problem is that Bundaberg Physio does not have an adequate bookkeeping system. This technical solution provided by this project is supposed to solve this problem, by providing patient and test storage for the business." ID="ID_821668383" CREATED="1675997351951" MODIFIED="1689304351159"/>
</node>
</node>
<node TEXT="Communication" POSITION="left" ID="ID_852974468" CREATED="1675380670585" MODIFIED="1689303817404" HGAP_QUANTITY="-75.25 pt" VSHIFT_QUANTITY="-48 pt">
<edge COLOR="#7c0000"/>
<node TEXT="Mode-appropriate features, Conventions and Language" ID="ID_1897687996" CREATED="1675380688175" MODIFIED="1689303817404" HGAP_QUANTITY="33.5 pt" VSHIFT_QUANTITY="-9.75 pt">
<node TEXT="Language such as pseudocode and direct code will be used to analyse and explain how the code works, with the difference between direct code and pseudocode being that direct code is code taken from the files given to the interpreter, sometimes not being very easy to understand, whereas pseudocode is direct code adapted to be easier to read." ID="ID_1202415803" CREATED="1675396554893" MODIFIED="1676285842716" HGAP_QUANTITY="14 pt" VSHIFT_QUANTITY="4.5 pt"/>
<node TEXT="The documentation provided with this project will be using 8 to 10 A3 sized paper for everything but the code snippets, whcih will be in A4 sizing, with 4 to 6 pages made available. The A3 sections will be in primarily 11 point size text." ID="ID_288736924" CREATED="1675997367344" MODIFIED="1689303812402"/>
<node TEXT="The referencing for this project&apos;s documentation will be APA style." ID="ID_1036570647" CREATED="1675997375633" MODIFIED="1676285834433"/>
</node>
</node>
</node>
</map>
