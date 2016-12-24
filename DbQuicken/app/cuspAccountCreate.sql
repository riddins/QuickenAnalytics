CREATE PROCEDURE [app].[cuspAccountCreate]
	@ParentAccountId int = NULL,
	@TypeId int,
	@Name nvarchar(50),
	@Description nvarchar(50)
AS
	SET NOCOUNT ON
	INSERT INTO Account (ParentAccountId, TypeId, Name, [Description]) VALUES(@ParentAccountId, @TypeId, @Name, @Description)

	SELECT Id
	FROM Account
	WHERE Id = SCOPE_IDENTITY();

RETURN 0