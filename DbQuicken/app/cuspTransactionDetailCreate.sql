CREATE PROCEDURE [app].[cuspTransactionDetailCreate]
	@TransactionId int,
	@AccountId int, 
	@DebitCredit char(1),
	@Date date,
	@Num nvarchar(10) = NULL,
	@Amount decimal(10,2),
	@Cleared nvarchar(1) = NULL,
	@Payee nvarchar(50),
	@Memo nvarchar(100) = NULL,
	@Address nvarchar(100) = NULL,
	@Catagory nvarchar(50) = NULL,
	@ReimbursableExpense bit

AS
	SET NOCOUNT ON
	INSERT INTO TransactionDetail([TransactionId], [AccountId], [DebitCredit], [Date], [Num], [Amount], [Cleared], [Payee], [Memo], [Address], [Catagory], [ReimbursableExpense])
		VALUES (@TransactionId, @AccountId, @DebitCredit, @Date, @Num, @Amount, @Cleared, @Payee, @Memo, @Address, @Catagory, @ReimbursableExpense)

	SELECT Id
	FROM TransactionDetail
	WHERE Id = SCOPE_IDENTITY();

RETURN 0
