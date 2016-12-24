CREATE PROCEDURE [app].[cuspTransactionIdRead]
	@Id int = Null,
	@Status CHAR(1) = Null,
	@TransactionDescription NVARCHAR(50) = Null
AS
	SELECT trans.Id, trans.[Status], trans.TransactionDescription
	FROM dbo.TransactionId as trans
	WHERE (Id = @Id OR @Id is NULL)
		AND ([Status] = @Status OR @Status is NULL)
		AND (TransactionDescription = @TransactionDescription OR @TransactionDescription is NULL)

RETURN 0

