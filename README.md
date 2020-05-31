# Anti-Cheating-Exam

* Supervising examinations has been a manual task since the longest of times but involves various factors which makes it not the best way to supervise examination.
* Our proposed system provides an information technology approach towards curbing the problem of cheating in examination halls. We aim to develop such a system which can be used to prevent cheating in examination hall by alerting the concerned faculty using various attributes such as head movement and eye movement. The algorithm first detects the faces from the video stream generated by the surveillance cameras (CCTVs), then picks up each face, then recognizes, analyzes the head as well as tracks eyes movement and on amalgamating the various information infers whether or not that student is involved in cheating. We can also provide digital evidence of the students involved in cheating before the institution’s disciplinary committee.


### Requirements
- mtcnn
- dlib
- tensorflow
- keras
- opencv


### Dataset
- Pandora (for faces)
- Unityeyes (for eyes)


### Output
(output.png)

### How to run demo.
- Create final_datset/test folder and save 4 videos (which are to be evaluated) inside it .
- Open demo notebook and run all cell.
- For testing using web cam uncomment second last cell and run it.
- To see the live graph run the suspecious_level_plot.py file from the cmd after commpleting above steps.



