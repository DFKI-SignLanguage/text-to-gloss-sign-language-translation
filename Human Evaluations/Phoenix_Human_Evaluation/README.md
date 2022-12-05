# Streamlit evaluation interface

## For Mac & Windows user:

1. Clone the repository or download the repository
 
        git clone https://github.com/DFKI-SignLanguage/text-to-gloss-sign-language-translation.git
        
2. Install the Python3 (Better the newest version)
3. Open the Terminal and change directory to
        
        cd ./text-to-gloss-sign-language-translation/Human Evaluations/Phoenix_Human_Evaluation

4. Install the Python Requirements

        pip3 install -r requirements.txt

5. Run app.py

        streamlit run app.py

Open the browser at http://localhost:8501/

## The interface
<img src="https://github.com/yvanzhu/Sign_language_human_evaluation/blob/main/Phoenix_evaluation_new/Interface.png" width="400" height="600" alt="Image text"/><br/>

1. If you think it is a bad reference either in source side or target side, click the top button of the interface. You may also have to score the predictions to finalize the evaluation.

2. Score slider counts from 0 to 6 in integer. 

3. Leave comments if you think it is necessary to explain. 

4. The predictions of each system are randomly arranged.

5. A big drawback of this interface: <font color=red>**_YOU CAN NOT SHUT DOWN THE TERMINAL AND WEB UNTIL EVALUATION FINISHED_**</font>. 

  If you need multiple times to finish all the evaluation, every time you need pause, just click "EXIT & PAUSE" and then keep the web interface and Terminal on. When you go back to evaluation, click the "BACK TO EVALUATION", you will back to the page and continue evaluation. 

5. At the end, you will find the file "FEEDBACK_PHOENIX.txt" under the directory.
