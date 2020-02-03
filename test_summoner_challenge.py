#!/usr/bin/env python3

import pandas as pd
import unittest
import summoner_challenge

class Teste(unittest.TestCase):
    def test_calculateDPS(self):
        data_mock     = {'ATTACK_SPEED': [3, 2, 1, 0], 'ATTACK_DAMAGE': [6, 9, 12, 15]}
        df_mock       = pd.DataFrame.from_dict(data_mock)
        data_expected = {'ATTACK_SPEED': [3, 2, 1, 0], 'ATTACK_DAMAGE': [6, 9, 12, 15], 'DPS': [18, 18, 12, 0]}
        df_expected   = pd.DataFrame.from_dict(data_expected)        
        df_result     = summoner_challenge.calculateDPS(df_mock)
        
        self.assertTrue(df_result.equals(df_expected))

    def test_removeColumn(self):
           
        data_mock     = {'ATTACK_SPEED': [3, 2, 1, 0], 'ATTACK_DAMAGE': [6, 9, 12, 15]}
        df_mock       = pd.DataFrame.from_dict(data_mock)        
        df_result     = summoner_challenge.DataPrep.removeColumn(df_mock, 'ATTACK_DAMAGE')
        data_expected = {'ATTACK_SPEED': [3, 2, 1, 0]}
        df_expected   = pd.DataFrame.from_dict(data_expected)

        self.assertTrue(df_result.equals(df_expected))

if __name__ == '__main__':
    unittest.main()
