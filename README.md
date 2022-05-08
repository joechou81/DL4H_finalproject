# DL4H_Final Project

This is a reproduction project of  "Junyi Gao, Cao Xiao, Yasha Wang, Wen Tang, Lucas MGlass, and Jimeng Sun. 2020. Stagenet: Stage-aware
neural networks for health risk prediction. In Proceedings of The Web Conference 2020, pages 530–540."

This project is accomplished by the following procedure:

1. Get access to the MIMIC-III database through Physionet (https://physionet.org/content/mimiciii/1.4/)
2. Create the benchmark dataset, especially for decompensation. The construction of the benchmark dataset can refer to "Hrayr Harutyunyan, Hrant Khachatrian, David C. Kale, Greg Ver Steeg, and Aram Galstyan. 2019. Multitask learning and benchmarking with clinical time series data. Scientific Data, 6(1):96". The reference Github repo can be found at https://github.com/YerevaNN/mimic3-benchmarks.
3. After downloading the files needed to create the benchmark dataset. Please check the panda version. If pandas version higher than 1.1.3, the attribute “ix” should be manually fixed to “loc” to make success run of the code. (In: ./mimic3benchmark/mimic3csv.py Line: 80)
4. StageNet model can be found at Github (https://github.com/v1xerunt/StageNet)
5. Copy the decompensation folder to the StageNet directory, which includes:
   - train folder (with training samples included)
   - test folder (with test samples included)
   - val_listlife.csv
   - test_listlife.csv
   - train_listlife.csv
6. Train StageNet with 256 training samples using the following command:
   ```
   python train.py --data_path='./data/' --file_name='trained_model' --small_part 1
   ```
   make sure that your current directory is in the StageNet folder.
7. StageNet, LSTM, T-LSTM, ON-LSTM, and 4 types of reduced model are implemented in model.py. By swithching the comment in Line 172 - 178 in train.py, different model can be trained. 

8. 
