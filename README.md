# DL4H_finalproject

This is a reproduction project of  "Junyi Gao, Cao Xiao, Yasha Wang, Wen Tang, Lucas MGlass, and Jimeng Sun. 2020. Stagenet: Stage-aware
neural networks for health risk prediction. In Proceedings of The Web Conference 2020, pages 530–540."

This project is accomplished by the following procedure:

1. Get access to the MIMIC-III database through Physionet (https://physionet.org/content/mimiciii/1.4/{Physionet)
2. Create the benchmark dataset, especially for decompensation. The construction of the benchmark dataset can refer to "Hrayr Harutyunyan, Hrant Khachatrian, David C. Kale, Greg Ver Steeg, and Aram Galstyan. 2019. Multitask learning and benchmarking with clinical time series data. Scientific Data, 6(1):96". The reference Github repo can be found at https://github.com/YerevaNN/mimic3-benchmarks.
3. After downloading the files needed to create the benchmark dataset. Please check the panda version. If pandas 1.1.3, the attribute “ix” should be manually fixed to “loc” to make success run of the code. (In: ./mimic3benchmark/mimic3csv.py Line: 80)
4. StageNet model can be found at Github (https://github.com/v1xerunt/StageNet)
5. Copy the decompensation folder to the StageNet directory, which includes:
   - train folder (with training samples included)
   - test folder (with test samples included)
   - val_listlife.csv
   - test_listlife.csv
   - train_listlife.csv
6. Train StageNet with 256 training samples using the following command:
        python train.py --data_path='./data/' --file_name='trained_model' --small_part 1
   make sure that your current directory is in the StageNet folder.
7. The lstm model can also be found in the benchmark folder (mimic3models/keras_models/lstm.py). The detailed steps is in https://github.com/YerevaNN/mimic3-benchmarks.
8. Implementation of T-LSTM and ON-LSTM (uncomplete).
9. Implementation of two reduced StageNets as mentioned in the paper(uncomplete).
10. Compare accuracy of LSTM, T-LSTM, ON-LSTM, StageNet, Reduced StageNet(uncomplete).
11. Finetune hyperparameters of StageNet.