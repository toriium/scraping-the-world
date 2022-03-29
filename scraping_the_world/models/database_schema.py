SCHEMA_DDL = """
create table if not exists sites_data
(
	id int auto_increment
		primary key,
	title varchar(100) null,
	preco varchar(50) null,
	imagem varchar(50) null,
	descricao varchar(500) null,
	url_recebida varchar(500) null,
	data_verificado datetime default current_timestamp() null,
	url_site varchar(500) null
);

"""
