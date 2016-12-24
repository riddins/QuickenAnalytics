CREATE TABLE [dbo].[Account]
(
	[Id] INT NOT NULL PRIMARY KEY IDENTITY
	,[ParentAccountId] INT NULL
	,[TypeId] INT NOT NULL
	,[Name] NVARCHAR(50) NOT NULL
	,[Description] NVARCHAR(50) NULL
	CONSTRAINT [FK_Account_ParentAccount] FOREIGN KEY ([ParentAccountId]) REFERENCES [Account]([Id])
	,CONSTRAINT [FK_Account_AccountType] FOREIGN KEY ([TypeId]) REFERENCES [AccountType]([Id])
)
