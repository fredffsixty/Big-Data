# Progetto di esame a.a. 2020-2021

Il progetto è una competizione Kaggle che si trova al [seguente indirizzo](https://www.kaggle.com/mlg-ulb/creditcardfraud).

Si tratta di un data set di frodi su carte di credito in cui sono presenti solo 492 frodi su 284.807 transazioni.

I dati contengono i seguenti campi:

    - Time: un identificativo numerico prograssivo della transazione
    - V1 ... V28: feature di dettaglio della transazione convertite con la PCA per questioni di privacy
    - Amount: ammntare della transazione
    - Class: 0/1 per indicare transazione normale/fraudolenta

Si richiede di effettuare tutti i passi di data cleaning/inputation e una analisi delle feature rilevanti ai fini della classificazione. 

La metrica richiesta è la Area Under the Precision-Recall Curve (AUPRC).

I gruppi candidati dovranno inoltre trovare una modalità di visualizzazione dei dati classificati in 2D o 3D che consenta di mettere in relazione i punti appartenenti a ciascuna classe con le feature utilizzate per la classificazione ai fini di apprezzare l'effettiva separazione tra le classi.

Suggerimento: utilizzare il Multi-Dimensional Scaling (MDS).