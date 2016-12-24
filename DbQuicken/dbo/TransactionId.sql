CREATE TABLE [dbo].[TransactionId]
(
	[Id] INT NOT NULL PRIMARY KEY IDENTITY
	,[Status] CHAR(1) NOT NULL DEFAULT 'o'
	,[TransactionDescription] NVARCHAR(50) NULL

	/**** Status Values ****/
	-- 'o' = OPEN (DEFAULT):  Can post new TransactionDetail for this TransactionId
	-- 'c' = CLEARED:  All TransactionDetail has posted and Debits = Credits.  No new Transaction Detail can be posted
	-- 'v' = VOID:  Reserved for voiding the transaction and all realted detail
	-- 'r' = RECONCILED:  Reserved for reconciliation process
	-- 's' = STATIC:  Reserved for system use (e.g. unmatched transfers)

	CONSTRAINT [CK_TransactionId_Status] CHECK ([Status] IN ('o', 'c', 'v', 'r', 's'))
)
