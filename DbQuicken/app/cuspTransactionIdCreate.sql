CREATE PROCEDURE [app].[cuspTransactionIdCreate]
	@TransactionDescription as NVARCHAR(50) = NULL

AS
	SET NOCOUNT ON
	INSERT INTO TransactionId([Status], [TransactionDescription]) VALUES ('o', @TransactionDescription)

	SELECT Id
	FROM TransactionId
	WHERE Id = SCOPE_IDENTITY();

RETURN 0
