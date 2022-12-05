import streamlit as st 
import pandas as pd

test_german_ref= './refs/phoenix_test_sentences_lowercase.txt'
test_gloss_ref = './refs/phoenix_test_glosses_lowercase.txt'

test_gloss_system_3 = './outputs/BEST_SYSTEM.txt'
test_gloss_system_1 ='./outputs/BASELINE_1.txt'
test_gloss_system_2 = './outputs/BASELINE_2.txt'

human_evaluation_path = './FEEDBACK_PHOENIX.txt'

count= len(open('./refs/phoenix_test_sentences_lowercase.txt','r').readlines())

if 'num' not in st.session_state:
    st.session_state.num = 0
if 'data' not in st.session_state:
    st.session_state.data = []

class ScoreSys:
    def __init__(self, page_id):
        #st.subheader(f"Comment of No.{page_id}")
        self.comments = st.text_input("Comment here if avaliable")
 
def main():

    st.title('PHOENIX human evaluation system')
    placeholder = st.empty()
    placeholder2 = st.empty()
    while st.session_state.num <= count-1:    
        num = st.session_state.num
 
        if placeholder2.button('SAVE & PAUSE', key=num):

            placeholder2.empty()
            df = pd.DataFrame(st.session_state.data)
            st.dataframe(df)
            df.to_csv(human_evaluation_path, index = None, header = True, sep = '\t',columns=['Score1','Score2','Score3','Comment','BAD_REF'])
            break
        else:        
            with placeholder.form(key=str(num)):
                Bad_refs = st.checkbox('Click if it is a bad reference')

                df_ger_ref = pd.read_table(test_german_ref,header = None, names = ['PHOENIX GERMAN SENTENCE REFERENCE'])
                st.markdown(f'<u>**_PHOENIX GERMAN SENTENCE REFERENCE {num}_**</u>',unsafe_allow_html=True)
                st.markdown(f'<p style="font-family:Arial; color:White; font-size: 20px;">{df_ger_ref.iloc[int(num),0]}</p>', unsafe_allow_html=True)
            
                df_glo_ref = pd.read_table(test_gloss_ref,header = None, names = ['PHOENIX GLOSS REFERENCE'])
                st.markdown(f'<u>**_PHOENIX GLOSS REFERENCE {num}_**</u>',unsafe_allow_html=True)
                st.markdown(f'<p style="font-family:Arial; color:White; font-size: 20px;">{df_glo_ref.iloc[int(num),0]}</p>', unsafe_allow_html=True)

                list = [[1, 2, 3],[1,3,2],[2,1,3],[2,3,1],[3,2,1],[3,1,2],[1,3,2],[3,2,1],[1,2,3],[3,1,2],[2,3,1],[1,2,3]]
                term = {}
                a = 1
                #random.shuffle(list) # causing chaotic somehow
                for j in range(0,12):
                    if num % 12 == j:
                        for i in list[j]:
                            df = pd.read_table(f'./outputs/SYSTEM_{i}.txt', header = None, names = [f'PREDICTION_SYSTEM_{i}'])
                            st.markdown(f'<u>**_PREDICTION_{a}_**</u>',unsafe_allow_html=True)
                            st.markdown(f'<p style="font-family:Arial; font-size: 20px;">{df.iloc[int(num),0].lower()}</p>', unsafe_allow_html=True)
                            term['score{}'.format(i)] = st.slider(f'Score for prediction {a}', 0, 6, 0)
                            a += 1
                
                if num == count-1:
                    tile = '<p style="font-family:Arial; color:Red; font-size: 20px;"><u>This is the last page, Please click NEXT and then SAVE TO FILE & FINISH</u></p>'
                    st.markdown(tile, unsafe_allow_html=True)
                
                systems = ScoreSys(page_id=num)  
                
                st.progress((num+1)/count)
                st.write(num+1, 'out of', count)      
                if num <= count-1:
                    if st.form_submit_button('NEXT'): 
                        if Bad_refs:               
                            st.session_state.data.append({
                        'Score1':  term['score1'],
                        'Score2':  term['score2'],
                        'Score3':  term['score3'],
                        'Comment': systems.comments,
                        'BAD_REF': 1})
                        else:
                            st.session_state.data.append({
                        'Score1':  term['score1'],
                        'Score2':  term['score2'],
                        'Score3':  term['score3'],
                        'Comment': systems.comments,
                        'BAD_REF': 0})
                        st.session_state.num += 1

                        placeholder.empty()
                        placeholder2.empty()
                
                    elif st.form_submit_button('PREVIOUS'):
                        st.session_state.data.pop()
                        st.session_state.num -= 1
                    else:
                        st.stop()

    if st.session_state.num <= count-1:
        if placeholder2.button('BACK TO EVALUATION'):
            placeholder2.empty()
            df = pd.DataFrame(st.session_state.data)
            st.dataframe(df)
            df.to_csv(human_evaluation_path, index=None, header = True, sep = '\t',columns=['Score1','Score2','Score3','Comment','BAD_REF'])
    else:
        if placeholder2.button('SAVE TO FILE & FINISH'):
            placeholder2.empty()
            df = pd.DataFrame(st.session_state.data)
            st.subheader('Overview of the evaluation')
            st.dataframe(df)
            df.to_csv(human_evaluation_path, index=None, header = True, sep = '\t',columns=['Score1','Score2','Score3','Comment','BAD_REF'])
            text = '<p style="font-family:Arial; font-size: 25px;"><u>Thanks for your time and wish you a very good day</u></p>'
            st.markdown(text, unsafe_allow_html=True)

main()