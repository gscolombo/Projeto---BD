import streamlit as st
import pandas as pd
import plotly.express as px

from typing import Literal

from request_utils import get_employee_stats


def employee_per_company(data: pd.DataFrame):
    fig_employees = px.bar(
        data,
        x='nome_fantasia',
        y='quant_funcionarios',
        title='Funcionários por Empresa',
        labels={'nome_fantasia': 'Empresa',
                'quant_funcionarios': 'Número de Funcionários'},
        color='quant_funcionarios',
        color_continuous_scale='blues'
    )
    fig_employees.update_layout(showlegend=False)
    st.plotly_chart(fig_employees, use_container_width=True)


def average_age_per_company(data: pd.DataFrame):
    fig_age = px.bar(
        data,
        x='nome_fantasia',
        y='idade_media',
        title='Idade Média por Empresa',
        labels={'nome_fantasia': 'Empresa', 'idade_media': 'Idade Média'},
        color='idade_media',
        color_continuous_scale='greens'
    )
    fig_age.update_layout(showlegend=False)
    st.plotly_chart(fig_age, use_container_width=True)


def gender_distribution_per_company(data: pd.DataFrame):
    gender_data = []
    for _, company in data.iterrows():
        gender_data.append({
            'Empresa': company['nome_fantasia'],
            'Gênero': 'Homens',
            'Percentual': company['proporcao_homens']
        })
        gender_data.append({
            'Empresa': company['nome_fantasia'],
            'Gênero': 'Mulheres',
            'Percentual': 100 - company['proporcao_homens']
        })

    gender_df = pd.DataFrame(gender_data)

    fig_gender = px.bar(
        gender_df,
        x='Empresa',
        y='Percentual',
        color='Gênero',
        title='Distribuição de Gênero por Empresa',
        barmode='stack',
        color_discrete_map={'Homens': '#1f77b4', 'Mulheres': '#ff7f0e'}
    )
    st.plotly_chart(fig_gender, use_container_width=True)


def gender_distribution(data: pd.DataFrame):
    total_men = data['proporcao_homens'].mean()
    fig_overall_gender = px.pie(
        values=[total_men, 100 - total_men],
        names=['Homens', 'Mulheres'],
        title='Distribuição Geral de Gênero',
        color=['Homens', 'Mulheres'],
        color_discrete_map={'Homens': '#1f77b4', 'Mulheres': '#ff7f0e'}
    )
    st.plotly_chart(fig_overall_gender, use_container_width=True)


def role_distribution_per_company(data: pd.DataFrame):
    roles_data = []
    for _, company in data.iterrows():
        roles_data.append({
            'Empresa': company['nome_fantasia'],
            'Cargo': 'Motoristas',
            'Percentual': company['proporcao_motorista']
        })
        roles_data.append({
            'Empresa': company['nome_fantasia'],
            'Cargo': 'Cobradores',
            'Percentual': company['proporcao_cobrador']
        })
        roles_data.append({
            'Empresa': company['nome_fantasia'],
            'Cargo': 'Fiscais',
            'Percentual': company['proporcao_fiscal']
        })

    roles_df = pd.DataFrame(roles_data)

    fig_roles = px.bar(
        roles_df,
        x='Empresa',
        y='Percentual',
        color='Cargo',
        title='Distribuição Percentual de Cargos por Empresa',
        barmode='stack',
        color_discrete_map={
            'Motoristas': '#2E86AB',
            'Cobradores': '#A23B72',
            'Fiscais': '#F18F01'
        },
        labels={'Percentual': 'Percentual (%)'}
    )
    fig_roles.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_roles, use_container_width=True)


def role_vs_mean_age(data: pd.DataFrame, role: Literal["Motorista", "Cobrador", "Fiscal"]):
    fig = px.scatter(
        data,
        y=f'proporcao_{role.lower()}',
        x='idade_media',
        color='quant_funcionarios',
        size='quant_funcionarios',
        hover_name='nome_fantasia',
        title=f'% {role} vs Idade Média',
        labels={
            f'proporcao_{role.lower()}': f'% {role}',
            'idade_media': 'Idade Média',
            'quant_funcionarios': 'Total Funcionários'
        },
    )
    fig.update_layout(showlegend=False,
                      coloraxis=dict(
                          colorbar=dict(
                              orientation='h',
                              y=.9,
                              x=.7,
                              xanchor='center'
                          )
                      ))
    st.plotly_chart(fig, use_container_width=True)


def cashier_vs_mean_age(data: pd.DataFrame):
    fig_scatter_cobrador = px.scatter(
        data,
        y='proporcao_cobrador',
        x='idade_media',
        size='quant_funcionarios',
        hover_name='nome_fantasia',
        title='Cobradores vs Idade Média (cor: % Homens)',
        labels={
            'proporcao_cobrador': '% Cobradores',
            'idade_media': 'Idade Média',
            'quant_funcionarios': 'Total Funcionários'
        },
    )
    fig_scatter_cobrador.update_layout(showlegend=False)
    st.plotly_chart(fig_scatter_cobrador, use_container_width=True)


def fiscal_vs_mean_age(data: pd.DataFrame):
    fig_scatter_fiscal = px.scatter(
        data,
        y='proporcao_fiscal',
        x='idade_media',
        size='quant_funcionarios',
        hover_name='nome_fantasia',
        title='Fiscais vs Idade Média (cor: % Homens)',
        labels={
            'proporcao_fiscal': '% Fiscais',
            'idade_media': 'Idade Média',
            'quant_funcionarios': 'Total Funcionários'
        },
    )
    fig_scatter_fiscal.update_layout(showlegend=False)
    st.plotly_chart(fig_scatter_fiscal, use_container_width=True)


def show_employee_stats():
    st.subheader("📈 Estatísticas de Funcionários por Empresa")

    # Get employee statistics
    employee_stats = get_employee_stats()

    if employee_stats:
        # Convert to DataFrame
        stats_df = pd.DataFrame(employee_stats)

        # Format numeric columns
        stats_df['proporcao_homens'] = (
            stats_df['proporcao_homens'] * 100).round(1)
        stats_df['proporcao_motorista'] = (
            stats_df['proporcao_motorista'] * 100).round(1)
        stats_df['proporcao_cobrador'] = (
            stats_df['proporcao_cobrador'] * 100).round(1)
        stats_df['proporcao_fiscal'] = (
            stats_df['proporcao_fiscal'] * 100).round(1)
        stats_df['idade_media'] = stats_df['idade_media'].round(1)
        stats_df['quant_funcionarios'] = stats_df['quant_funcionarios'].astype(
            int)

        # Create charts
        col1, col2 = st.columns(2)

        with col1:
            employee_per_company(stats_df)

        with col2:
            average_age_per_company(stats_df)

        # Gender distribution
        st.subheader("Distribuição de Gênero por Empresa")
        col1, col2 = st.columns([2, 1])

        with col1:
            gender_distribution_per_company(stats_df)

        with col2:
            gender_distribution(stats_df)

        # Job roles distribution
        st.subheader("Distribuição de Cargos por Empresa")

        role_distribution_per_company(stats_df)

        st.subheader("🔍 Análise de Relações: Cargos vs Demografia")

        col1, col2, col3 = st.columns(3)

        with col1:
            role_vs_mean_age(stats_df, "Motorista")
        with col2:
            role_vs_mean_age(stats_df, "Cobrador")
        with col3:
            role_vs_mean_age(stats_df, "Fiscal")

    else:
        st.info("Não foi possível carregar as estatísticas de funcionários.")
