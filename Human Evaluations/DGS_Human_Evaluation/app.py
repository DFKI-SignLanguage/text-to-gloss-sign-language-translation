import streamlit as st 
import pandas as pd

test_german_ref= './refs/samples_german_test.txt'
test_gloss_ref = './refs/samples_dgs_glosses_test_lower_all_cleaned.txt'
gloss_ori='./refs/samples_dgs_glosses_test_lower.txt'
human_evaluation_path = './FEEDBACK_DGS.txt'

count= round(len(open('./refs/samples_dgs_glosses_test_lower_all_cleaned.txt','r').readlines()))

if 'num' not in st.session_state:
    st.session_state.num = 0
if 'data' not in st.session_state:
    st.session_state.data = []

class ScoreSys:
    def __init__(self, page_id):
        #st.subheader(f"Comment of No.{page_id}")
        self.comments = st.text_input("Comment here if avaliable")
        
 
def main():

    st.title('DGS human evaluation system')
    placeholder = st.empty()
    placeholder2 = st.empty()
    while st.session_state.num <= count-1:    
        num = st.session_state.num
 
        if placeholder2.button('SAVE & PAUSE', key=num):

            placeholder2.empty()
            df = pd.DataFrame(st.session_state.data)
            st.dataframe(df)
            df.to_csv(human_evaluation_path, index = None, header = True, sep = '\t',columns=['Score1','Score2','Comment','BAD_REF'])
            break
        else:        
            with placeholder.form(key=str(num)):
                #Bad_refs = st.checkbox('Click if it is a bad reference')
                

                df_ger_ref = pd.read_table(test_german_ref,header = None, names = ['DGS GERMAN SENTENCE REFERENCE'])
                st.markdown(f'<u>**_DGS GERMAN SENTENCE REFERENCE {num}_**</u>',unsafe_allow_html=True)
                st.markdown(f'<p style="font-family:Arial; font-size: 20px;">{df_ger_ref.iloc[int(num),0]}</p>', unsafe_allow_html=True)
                df_glo_ref1 = pd.read_table(gloss_ori,header = None, names = ['DGS GLOSS REFERENCE'])
                st.markdown(f'<u>**_DGS GLOSS REFERENCE {num}_**</u>',unsafe_allow_html=True)
                st.markdown(f'<p style="font-family:Arial; font-size: 20px;">{df_glo_ref1.iloc[int(num),0]}</p>', unsafe_allow_html=True)
            
                df_glo_ref = pd.read_table(test_gloss_ref,header = None, names = ['GENERALIZED GLOSS REFERENCE'])
                st.markdown(f'<u>**GENERALIZED GLOSS REFERENCE {num}_**</u>',unsafe_allow_html=True)
                st.markdown(f'<p style="font-family:Arial; font-size: 20px;">{df_glo_ref.iloc[int(num),0]}</p>', unsafe_allow_html=True)
                Bad_refs = st.slider(f'How bad is the Reference? Keep 0 if it is ok', 0, 6, 0)
                list = [[1, 2],[1,2],[2,1],[2,1],[2,1],[1,2],[1,2],[2,1],[1,2],[1,2],[2,1],[1,2]]
                term = {}
                a = 1
                #random.shuffle(list) # causing chaotic somehow
                for j in range(0,12):
                    if num % 12 == j:
                        for i in list[j]:
                            df = pd.read_table(f'./outputs/samples_SYSTEM_{i}.txt', header = None, names = [f'PREDICTION_SYSTEM_{i}'])
                            st.markdown(f'<u>**_PREDICTION_{a}_**</u>',unsafe_allow_html=True)
                            st.markdown(f'<p style="font-family:Arial; font-size: 20px;">{df.iloc[int(num),0].lower()}</p>', unsafe_allow_html=True)
                            term['score{}'.format(i)] = st.slider(f'Score for prediction {a}', 0, 6, 0)
                            a += 1
                
                if num == count-1:
                    tile = '<p style="font-family:Arial; color:Red; font-size: 20px;"><u>This is the last page, Please click NEXT and then SAVE TO FILE & FINISH</u></p>'
                    st.markdown(tile, unsafe_allow_html=True)
                
                systems = ScoreSys(page_id=num)  
                
                st.progress((num+1)/count)
                st.write(num+1, 'of', count)      
                if num <= count-1:
                    if st.form_submit_button('NEXT'): 
 
                        st.session_state.data.append({
                        'Score1':  term['score1'],
                        'Score2':  term['score2'],
                        'Comment': systems.comments,
                        'BAD_REF': Bad_refs})

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
            df.to_csv(human_evaluation_path, index=None, header = True, sep = '\t',columns=['Score1','Score2','Comment','BAD_REF'])
    else:
        if placeholder2.button('SAVE TO FILE & FINISH'):
            placeholder2.empty()
            df = pd.DataFrame(st.session_state.data)
            st.subheader('Overview of the evaluation')
            st.dataframe(df)
            df.to_csv(human_evaluation_path, index=None, header = True, sep = '\t',columns=['Score1','Score2','Comment','BAD_REF'])
            text = '<p style="font-family:Arial; font-size: 25px;"><u>Thanks for your time and wish you a very good day</u></p>'
            st.markdown(text, unsafe_allow_html=True)

main()