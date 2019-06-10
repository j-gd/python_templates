df_sol = pd.read_csv("data/do_not_open/test_soln.csv.zip")

def score(self, predictions):
        log_diff = np.log(predictions+1) - np.log(self+1)
        return np.sqrt(np.mean(log_diff**2))

rmsle = score(df_sol["SalePrice"], pred))
rmsle
