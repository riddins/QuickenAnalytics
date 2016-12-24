CREATE PROCEDURE [app].[cuspTransactionDetailRead]
	@Id int = NULL,
	@TransactionId int = NULL,
	@AccountId int = NULL, 
	@DebitCredit char(1) = NULL,
	@Date date = NULL,
	@Num nvarchar(10) = NULL,
	@Amount decimal(10,2) = NULL,
	@Cleared nvarchar(1) = NULL,
	@Payee nvarchar(50) = NULL,
	@Memo nvarchar(100) = NULL,
	@Address nvarchar(100) = NULL,
	@Catagory nvarchar(50) = NULL,
	@ReimbursableExpense bit = NULL
AS
	SELECT [Id], [TransactionId], [AccountId], [DebitCredit], [Date], [Num], [Amount], [Cleared]
		, [Payee], [Memo], [Address], [Catagory], [ReimbursableExpense]
	FROM TransactionDetail
	WHERE (Id = @Id OR @Id is NULL)
		AND (TransactionId = @TransactionId OR @TransactionId is NULL)
		AND (AccountId = @AccountId OR @AccountId is NULL)
		AND (DebitCredit = @DebitCredit OR @DebitCredit is NULL)
		AND ([Date] = @Date OR @Date is NULL)
		AND (Num = @Num OR @Num is NULL)
		AND (Amount = @Amount OR @Amount is NULL)
		AND (Cleared = @Cleared OR @Cleared is NULL)
		AND (Payee = @Payee OR @Payee is NULL)
		AND (Memo = @Memo OR @Memo is NULL)
		AND ([Address] = @Address OR @Address is NULL)
		AND (Catagory = @Catagory OR @Catagory is NULL)
		AND (ReimbursableExpense = @ReimbursableExpense OR @ReimbursableExpense is NULL)
RETURN 0
