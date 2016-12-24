CREATE PROCEDURE [app].[cuspAccountRead]
	@Id int = NULL,
	@Name nvarchar(50) = NULL,
	@TypeId int = NULL,
	@ParentAccountId int = NULL
AS
	SELECT acc.Id, acc.ParentAccountId, acc.TypeId, acc.Name, acc.[Description]
	FROM Account as acc
	WHERE (Id = @Id OR @Id is NULL)
		AND (Name = @Name OR @Name is NULL)
		AND (TypeId = @TypeId OR @TypeId is NULL)
		AND (ParentAccountId = @ParentAccountId OR @ParentAccountId is NULL)

RETURN 0
