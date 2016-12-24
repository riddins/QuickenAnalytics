CREATE TABLE [dbo].[TransactionDetail]
(
	[Id] INT NOT NULL PRIMARY KEY IDENTITY
	,[TransactionId] INT NOT NULL
	,[AccountId] INT NOT NULL 
	,[DebitCredit] CHAR(1) NOT NULL
	,[Date] DATE NOT NULL
	,[Num] NVARCHAR(10) NULL
	,[Amount] DECIMAL(10,2) NOT NULL
	,[Cleared] NVARCHAR(1) NULL
	,[Payee] NVARCHAR(50) NOT NULL
	,[Memo] NVARCHAR(100) NULL
	,[Address] NVARCHAR(100) NULL
	,[Catagory] NVARCHAR(50) NULL
	,[ReimbursableExpense] BIT NOT NULL, 
	
	CONSTRAINT [FK_TransactionDetail_Account] FOREIGN KEY ([AccountId]) REFERENCES [Account]([Id])
	,CONSTRAINT [FK_TransactionDetail_TransactionId] FOREIGN KEY ([TransactionId]) REFERENCES [TransactionId]([Id])
	,CONSTRAINT [CK_TransactionDetail_ToAccount] CHECK ([DebitCredit] = 'D' OR [DebitCredit] = 'C') 

	 
)