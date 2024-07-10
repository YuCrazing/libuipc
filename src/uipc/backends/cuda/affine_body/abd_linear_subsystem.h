#pragma once
#include <linear_system/diag_linear_subsystem.h>
#include <affine_body/affine_body_dynamics.h>
#include <affine_body/abd_contact_receiver.h>
#include <affine_body/affine_body_vertex_reporter.h>
#include <affine_body/matrix_converter.h>

namespace uipc::backend::cuda
{
class ABDLinearSubsystem : public DiagLinearSubsystem
{
  public:
    using DiagLinearSubsystem::DiagLinearSubsystem;

    class Impl
    {
      public:
        void report_extent(GlobalLinearSystem::DiagExtentInfo& info);
        void assemble(GlobalLinearSystem::DiagInfo& info);
        void _assemble_gradient(GlobalLinearSystem::DiagInfo& info);
        void _assemble_hessian(GlobalLinearSystem::DiagInfo& info);
        void assemble_H12x12();
        void accuracy_check(GlobalLinearSystem::AccuracyInfo& info);
        void retrieve_solution(GlobalLinearSystem::SolutionInfo& info);

        AffineBodyDynamics*       affine_body_dynamics = nullptr;
        AffineBodyDynamics::Impl& abd() noexcept
        {
            return affine_body_dynamics->m_impl;
        }
        ABDContactReceiver*       abd_contact_receiver = nullptr;
        ABDContactReceiver::Impl& contact() noexcept
        {
            return abd_contact_receiver->m_impl;
        }
        AffineBodyVertexReporter* affine_body_vertex_reporter = nullptr;

        Float reserve_ratio       = 1.5;

        ABDMatrixConverter                   converter;
        muda::DeviceTripletMatrix<Float, 12> triplet_A;
        muda::DeviceBCOOMatrix<Float, 12>    bcoo_A;
    };

  protected:
    virtual void do_build(DiagLinearSubsystem::BuildInfo& info) override;
    virtual void do_report_extent(GlobalLinearSystem::DiagExtentInfo& info) override;
    virtual void do_assemble(GlobalLinearSystem::DiagInfo& info) override;
    virtual void do_accuracy_check(GlobalLinearSystem::AccuracyInfo& info) override;
    virtual void do_retrieve_solution(GlobalLinearSystem::SolutionInfo& info) override;

  private:
    Impl m_impl;
};
}  // namespace uipc::backend::cuda
