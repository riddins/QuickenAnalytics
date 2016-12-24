CREATE PROCEDURE [app].[cuspAccountTypeCreate]
	@AccountType nvarchar(50)
AS
	SET NOCOUNT ON
	INSERT INTO dbo.AccountType ([AccountType]) VALUES (@AccountType)

	SELECT Id
	FROM dbo.AccountType
	WHERE Id = SCOPE_IDENTITY();
RETURN 0
