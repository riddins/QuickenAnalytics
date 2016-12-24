CREATE PROCEDURE [app].[cuspAccountTypeRead]
	@Id int = NULL,
	@AccountType nvarchar(50) = NULL
AS
	SELECT Id, AccountType
	FROM AccountType
	WHERE (Id = @Id OR @Id is NULL)
		AND (AccountType = @AccountType OR @AccountType is NULL)
RETURN 0
