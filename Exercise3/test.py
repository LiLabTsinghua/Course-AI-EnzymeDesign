import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.metrics import r2_score
from scipy.stats import pearsonr
import glob

def Whole_dataset():
    # Calculate the whole dataset
    Pcc = pearsonr(Value, Predict_Label)[0]
    RMSE = np.sqrt(mean_squared_error(Value, Predict_Label))
    MAE = mean_absolute_error(Value, Predict_Label)
    r2 = r2_score(Value, Predict_Label)
    print('***The whole set***')
    print('Pcc:', Pcc, 'RMSE:', RMSE, 'MAE:', MAE, 'r2:', r2)


def test_dataset():
    # Calculate the test dataset
    Value_test = []
    Predict_Label_test = []
    for i in range(len(Training_test)):
        if Training_test[i] == 1:
            Value_test.append(Value[i])
            Predict_Label_test.append(Predict_Label[i])
    Value_test = np.array(Value_test)
    Predict_Label_test = np.array(Predict_Label_test)
    Pcc_test = pearsonr(Value_test, Predict_Label_test)[0]
    RMSE_test = np.sqrt(mean_squared_error(Value_test, Predict_Label_test))
    MAE_test = mean_absolute_error(Value_test, Predict_Label_test)
    r2_test = r2_score(Value_test, Predict_Label_test)
    # print('***Test set***')
    print('Pcc:', Pcc_test, 'RMSE:', RMSE_test, 'MAE:', MAE_test, 'r2:', r2_test)


def Wildtype_all_dataset():
    # Calculate the Wildtype/Mutant dataset
    Value_wildtype = []
    Predict_Label_wildtype = []
    for i in range(len(Type)):
        if Type[i] == 'wild':
            Value_wildtype.append(Value[i])
            Predict_Label_wildtype.append(Predict_Label[i])
    Value_wildtype = np.array(Value_wildtype)
    Predict_Label_wildtype = np.array(Predict_Label_wildtype)
    Pcc_test = pearsonr(Value_wildtype, Predict_Label_wildtype)[0]
    RMSE_test = np.sqrt(mean_squared_error(Value_wildtype, Predict_Label_wildtype))
    MAE_test = mean_absolute_error(Value_wildtype, Predict_Label_wildtype)
    r2_test = r2_score(Value_wildtype, Predict_Label_wildtype)
    print('***The whole wildtype set***')
    print('Pcc:', Pcc_test, 'RMSE:', RMSE_test, 'MAE:', MAE_test, 'r2:', r2_test)


def Wildtype_test_dataset():
    # Calculate the Wildtype/Mutant dataset
    Value_wildtype = []
    Predict_Label_wildtype = []
    for i in range(len(Type)):
        if Type[i] == 'wild' and Training_test[i] == 1:
            Value_wildtype.append(Value[i])
            Predict_Label_wildtype.append(Predict_Label[i])
    Value_wildtype = np.array(Value_wildtype)
    Predict_Label_wildtype = np.array(Predict_Label_wildtype)
    Pcc_test = pearsonr(Value_wildtype, Predict_Label_wildtype)[0]
    RMSE_test = np.sqrt(mean_squared_error(Value_wildtype, Predict_Label_wildtype))
    MAE_test = mean_absolute_error(Value_wildtype, Predict_Label_wildtype)
    r2_test = r2_score(Value_wildtype, Predict_Label_wildtype)
    print('***The test wildtype set***')
    print('Pcc:', Pcc_test, 'RMSE:', RMSE_test, 'MAE:', MAE_test, 'r2:', r2_test)


def Mutant_all_dataset():
    # Calculate the Wildtype/Mutant dataset
    Value_wildtype = []
    Predict_Label_wildtype = []
    for i in range(len(Type)):
        if Type[i] != 'wild':
            Value_wildtype.append(Value[i])
            Predict_Label_wildtype.append(Predict_Label[i])
    Value_wildtype = np.array(Value_wildtype)
    Predict_Label_wildtype = np.array(Predict_Label_wildtype)
    Pcc_test = pearsonr(Value_wildtype, Predict_Label_wildtype)[0]
    RMSE_test = np.sqrt(mean_squared_error(Value_wildtype, Predict_Label_wildtype))
    MAE_test = mean_absolute_error(Value_wildtype, Predict_Label_wildtype)
    r2_test = r2_score(Value_wildtype, Predict_Label_wildtype)
    print('***The whole mutant set***')
    print('Pcc:', Pcc_test, 'RMSE:', RMSE_test, 'MAE:', MAE_test, 'r2:', r2_test)


def Mutant_test_dataset():
    # Calculate the Wildtype/Mutant dataset
    Value_wildtype = []
    Predict_Label_wildtype = []
    for i in range(len(Type)):
        if Type[i] != 'wild' and Training_test[i] == 1:
            Value_wildtype.append(Value[i])
            Predict_Label_wildtype.append(Predict_Label[i])
    Value_wildtype = np.array(Value_wildtype)
    Predict_Label_wildtype = np.array(Predict_Label_wildtype)
    Pcc_test = pearsonr(Value_wildtype, Predict_Label_wildtype)[0]
    RMSE_test = np.sqrt(mean_squared_error(Value_wildtype, Predict_Label_wildtype))
    MAE_test = mean_absolute_error(Value_wildtype, Predict_Label_wildtype)
    r2_test = r2_score(Value_wildtype, Predict_Label_wildtype)
    print('***The test mutant set***')
    print('Pcc:', Pcc_test, 'RMSE:', RMSE_test, 'MAE:', MAE_test, 'r2:', r2_test)


def New_substrate_enzyme_dataset():
    # Calculate the test New_substrate_enzyme dataset
    Trainingset_seq_smiles = []
    for i in range(len(Training_test)):
        if Training_test[i] == 0:
            Trainingset_seq_smiles.append(sequence[i])
            Trainingset_seq_smiles.append(smiles[i])
    Value_test = []
    Predict_Label_test = []
    for i in range(len(Training_test)):
        if Training_test[i] == 1 and (sequence[i] not in Trainingset_seq_smiles or smiles[i] not in Trainingset_seq_smiles):
            Value_test.append(Value[i])
            Predict_Label_test.append(Predict_Label[i])
    Value_test = np.array(Value_test)
    Predict_Label_test = np.array(Predict_Label_test)
    Pcc_test = pearsonr(Value_test, Predict_Label_test)[0]
    RMSE_test = np.sqrt(mean_squared_error(Value_test, Predict_Label_test))
    MAE_test = mean_absolute_error(Value_test, Predict_Label_test)
    r2_test = r2_score(Value_test, Predict_Label_test)
    print('***The Test new_substrate_enzyme dataset***')
    print('Pcc:', Pcc_test, 'RMSE:', RMSE_test, 'MAE:', MAE_test, 'r2:', r2_test)
